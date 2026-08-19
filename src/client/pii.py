"""
PII-szűrő — magyar személyes/üzleti azonosítók maszkolása.

A cél: a pipeline (HyDE, embedding, generálás) és a run_log tábla SOSE
lásson nyers PII-t. A mask() a pipeline-hívás ELŐTT fut, az unmask()
csak a végfelhasználónak visszaadott válaszban oldja fel a maszkot,
ha az agent véletlenül visszaírta a maszkolt tokent.

Regex-alapú, nem tökéletes (pl. a TAJ-minta egyszerű 9 jegyű szám,
ami elméletben más 9 jegyű számmal is ütközhet) — demóhoz elég.
"""
import re

# Sorrend számít: előbb a specifikusabb (kötőjeles, @ jeles) minták,
# hogy ne "egyék meg" egymás számjegyeit egy általánosabb minta.
_PATTERNS = [
    ("EMAIL", re.compile(r'\b[\w.+-]+@[\w-]+\.[\w.-]+\b')),
    ("BANKSZAMLA", re.compile(r'\b\d{8}-\d{8}(?:-\d{8})?\b')),
    ("ADOSZAM", re.compile(r'\b\d{8}-\d-\d{2}\b')),
    ("ADOAZONOSITO", re.compile(r'\b8\d{9}\b')),
    ("PHONE", re.compile(r'(?:\+36|06)[\s\-]?\(?\d{1,2}\)?[\s\-]?\d{3}[\s\-]?\d{3,4}\b')),
    ("TAJ", re.compile(r'\b\d{3}[\s\-]?\d{3}[\s\-]?\d{3}\b')),
]


def mask(text: str) -> tuple[str, dict[str, str]]:
    """
    Lecseréli a felismert PII-mintákat [TIPUS_N] placeholderekre.

    Visszaad: (maszkolt_szöveg, mapping) — a mapping {placeholder: eredeti_érték}.
    """
    mapping: dict[str, str] = {}
    masked = text

    for label, pattern in _PATTERNS:
        counter = [0]

        def _replace(m: re.Match, label=label, counter=counter) -> str:
            counter[0] += 1
            placeholder = f"[{label}_{counter[0]}]"
            mapping[placeholder] = m.group(0)
            return placeholder

        masked = pattern.sub(_replace, masked)

    return masked, mapping


def unmask(text: str, mapping: dict[str, str]) -> str:
    """Visszaállítja az eredeti értékeket a placeholderek helyén."""
    for placeholder, original in mapping.items():
        text = text.replace(placeholder, original)
    return text

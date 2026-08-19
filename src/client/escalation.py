"""
Eszkalációs logika az ügyfél-belépőponthoz.

Két FÜGGETLEN ok miatt eszkalálunk kollégához, ahelyett hogy az agent
választ generálna:
  1. score alapú  — a rerank nem talált elég releváns forrást (bizonytalan válasz)
  2. szabály alapú — a kérdés olyan témát érint, amit tudatosan nem akarunk
                      automatizált szöveggel megválaszolni (árazási alku,
                      jogi kötelezettségvállalás)

A szabály alapú ellenőrzés egy egyszerű kulcsszólista — nincs LLM-osztályozó,
mert ez egy demó, és a kulcsszavak jól lefedik a kért eseteket.
"""

SCORE_THRESHOLD = 0.3

# kulcsszó -> eszkalációs ok címke
_RULE_KEYWORDS = {
    "egyedi árazás": "custom_pricing",
    "egyedi ár": "custom_pricing",
    "kedvezmény": "discount",
    "keretszerződés": "framework_contract",
    "garanci": "guarantee",       # garancia, garantál, garantálnak stb.
    "nda": "nda",
    "titoktartás": "nda",
    "titoktartási": "nda",
}


def check_rule_based(question: str) -> str | None:
    """
    Kulcsszó-egyezés a kérdésben. Ha talál, visszaadja az eszkalációs okot,
    egyébként None.
    """
    q = question.lower()
    for keyword, reason in _RULE_KEYWORDS.items():
        if keyword in q:
            return reason
    return None


def check_score_based(top_rerank_score: float | None) -> str | None:
    """Ha a top rerank score None vagy a küszöb alatt van, eszkalálunk."""
    if top_rerank_score is None or top_rerank_score < SCORE_THRESHOLD:
        return "low_score"
    return None

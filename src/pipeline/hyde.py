"""
HyDE — Hypothetical Document Embedding.

Az elv: ahelyett, hogy a kérdést vektorizálnánk (ami nem hasonlít
az indexelt dokumentumokra), generálunk egy "ideális választ" Claude
Haiku-val, és azt vektorizáljuk. A hipotézis-válasz vektortere közelebb
van a tényleges dokumentumok vektorteréhez.

Ajánlatírás use case-nél: "Milyen módszertannal mérhető márkaismertség?"
→ Haiku generál egy módszertani bekezdést → az közelebb lesz az indexelt
  módszertani szövegekhez, mint maga a kérdés.
"""
import anthropic
from src.config import ANTHROPIC_API_KEY, HYDE_MODEL

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

HYDE_SYSTEM = """Te egy tapasztalt piackutatási szakértő vagy az NRC-nél.
A felhasználó kérdésére írj egy rövid (2-4 mondatos) szakmai választ,
mintha az egy módszertani leírásból vagy ajánlatból lennék kivéve.
Magyar nyelven válaszolj. Ne kérdezz vissza, csak írj."""


def generate_hypothesis(question: str) -> str:
    """
    Generál egy hipotézis-dokumentumot a kérdéshez.
    Ez kerül majd vektorizálásra a retrieval során.
    """
    response = client.messages.create(
        model=HYDE_MODEL,
        max_tokens=300,
        system=HYDE_SYSTEM,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text

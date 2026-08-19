# HF5 — Scope-specifikáció

**Projekt:** NRC kutatástervező asszisztens — az ügyfélirányú bejárat
**Alaprendszer:** `hf3-nrc-rag` (meglévő pipeline, változatlan retrieval-lánc)
**Dátum:** 2026.08.17
**Státusz:** jóváhagyásra vár

---

## 1 / Egy mondat

Az NRC megbízója a saját üzleti kérdését írja le a saját nyelvén, és percek alatt kap egy
módszertani javaslatot — melyik módszer, miért az, mekkora minta, mennyi idő —
forrásmegjelöléssel; a javaslat csak a kutatási vezető jóváhagyása után jut el hozzá.

## 2 / Mit old meg és mit nem

**Megoldja** (a tíz fájdalomból):

| # | Fájdalom | Hogyan |
|---|---|---|
| 1 | munkaidőn kívül nincs válasz | az asszisztens folyamatosan elérhető, a jóváhagyás aszinkron |
| 2 | ugyanazt magyarázzuk naponta | a módszertani alapkérdésekre a tudásbázis válaszol |
| 5 | személyre szabás csak a nagyoknak | a kis megbízó is kap módszertani javaslatot, nem árlistát |
| 7 | hetekig tart az ajánlati kör | a módszertani egyeztetés első köre percekre rövidül |

**Részben oldja meg:** 6 — a napló gyűjti a kérdéseket, de az elemzésük emberi munka marad.

**Nem oldja meg, és ezt kimondjuk:** 4 (ügystátusz-követés), 8 (sürgősségi triage),
10 (churn-előjelzés). Ezekhez CRM- és projektrendszer-integráció kell, ami nincs scope-ban.

## 3 / Mit csinál a rendszer

Egy folyamat, egy végigvitt eset, egy emberi jóváhagyási pont.

1. A megbízó beírja az üzleti kérdését (szabad szöveg).
2. PII-előszűrő maszkol (lásd 6.).
3. A meglévő HF3 pipeline fut: HyDE → pgvector retrieval → Cohere rerank → Sonnet generálás.
4. A generált javaslat `pending_approval` állapotba kerül. **Az ügyfél még nem látja.**
5. A kutatási vezető felületén megjelenik a javaslat **és a hivatkozott források**.
   Szerkeszthet, jóváhagy vagy elutasít.
6. Jóváhagyás után `approved` — az ügyfél látja, forrásmegjelöléssel.

## 4 / Mit NEM csinál

- **Nem árazza az egyedi kutatást.** Standardizált, nyilvános listaáras terméknél
  (omnibusz) indikatív árat ad forrásmegjelöléssel; egyedi projektnél, egyedi
  kedvezménynél és szerződéses vállalásnál eszkalál. A határvonat: ami publikált
  árlistában szerepel, az idézhető; ami kalkulációt igényel, az emberi döntés.
- Nem köt szerződést, nem foglal terepidőt, nem ad kötelező érvényű árajánlatot.
  Minden ár indikatív, és ezt a válasz szövege is kimondja.
- Nem lát ügyféladatot, korábbi projektet, CRM-et. Csak a nyilvános módszertani tudásbázist.
- Nem tanul a beszélgetésekből: nincs finomhangolás, a tudásbázis csak ingesttel bővül.
- Nincs autentikáció és nincs bérlői izoláció — ez PoC, nem éles rendszer. Kimondjuk a dián.

## 5 / Az eszkalációs ág

A jóváhagyási kapu és az eszkaláció **két külön dolog**, mindkettőt demózzuk.

Eszkaláció akkor indul, ha bármelyik teljesül:

- a legjobb rerank score a küszöb alatt (kezdő érték: 0.35, a golden seten hangolandó)
- a kérdés egyedi árazást, kedvezményt vagy szerződéses vállalást érint
  (kulcsszólista + LLM-osztályozó). A publikált omnibusz-listaár **nem** vált ki eszkalációt.
- a kérdés a tudásbázison kívüli témára megy (a HF3 grounding-logikája már kezeli)

Ilyenkor a rendszer **nem találgat**: kimondja, hogy ezt kollégához továbbítja,
és létrehoz egy eszkalációs rekordot a naplóban. Ez a demó második, kötelező esete.

## 6 / PII-előszűrő

Regex-alapú réteg, bemenő és naplózott irányban egyaránt, pszeudonimizálással:
e-mail, magyar telefonszám, adószám, adóazonosító jel, TAJ, bankszámlaszám.
A maszkolt tokent (`[EMAIL_1]`) a válaszban visszahelyettesítjük.

**Amit kimondunk a dián:** ez egy réteg a négyből (adatosztályozás → hozzáférés-kontroll →
PII-szűrő → szolgáltatói szerződés), nem teljes védelem. A magyar nyelvű PII-detektálás
recallja tipikusan gyenge, ezért a szűrő nem helyettesíti a jóváhagyási kaput.

## 7 / Futásnapló — `run_log` tábla

A meglévő Postgresben, a mérési terv **egyetlen** adatforrása. Mezők:

| mező | tartalom |
|---|---|
| `id`, `created_at` | azonosító, időbélyeg |
| `session_id` | egy beszélgetés összefűzéséhez |
| `question_masked` | a kérdés PII-maszkolás **után** |
| `hyde_hypothesis` | a generált hipotézis |
| `top_sources` | hivatkozott chunk-ok azonosítója és forrása (JSON) |
| `top_rerank_score` | a legjobb találat pontszáma |
| `outcome` | `answered` / `escalated` / `rejected` |
| `escalation_reason` | ha eszkalált: melyik feltétel váltotta ki |
| `latency_ms` | teljes futásidő |
| `tokens_in`, `tokens_out`, `cost_usd` | providerenként bontva |
| `approval_status` | `pending` / `approved` / `edited` / `rejected` |
| `approver`, `approved_at` | ki és mikor hagyta jóvá |
| `edit_distance` | mennyit szerkesztett a jóváhagyó a szövegen |

Az `edit_distance` a legfontosabb minőségi metrika: ha a kutatási vezető minden javaslatot
átír, a rendszer nem működik, akkor sem, ha technikailag hibátlan.

**Amit soha nem naplózunk:** maszkolatlan kérdésszöveg, a megbízó azonosítója.

## 8 / Belépőpont

Minimál webes felület, két nézet: ügyfélnézet (kérdés + válasz + források) és
jóváhagyói nézet (várakozó javaslatok, források, szerkesztés, jóváhagy/elutasít).
Nincs auth, nincs design-rendszer. A demó három perc, a felület ne vigye el a figyelmet.

## 9 / Demó-forgatókönyv

1. **Happy path:** „Új ízvariánst indítanánk ősszel, gyorsan kellene tudni, ismerik-e
   a márkánkat és kinek pozicionáljuk. Mikor és mennyiért tudunk erre adatot kapni?"
   → az agent omnibuszt javasol, hivatkozza a listaárat, a kedvezménysávot, a következő
   indulási időpontot és a 4 napos átfutást, forrásmegjelöléssel
   → jóváhagyói nézet → jóváhagyás → ügyfél látja.
2. **Eszkaláció:** „Ez féléves trackingként kellene, három országban, és van egy
   keretünk — mennyi kedvezményt tudtok adni?"
   → nincs listaár, egyedi kalkuláció és kereskedelmi döntés kell
   → a rendszer nem találgat, eszkalál, a naplóban megjelenik a rekord.

## 10 / Lezárt és nyitott pontok

**Lezárva:** az omnibusz árlista nyilvános ügyfélprezentációból származik, ezért
publikus repóban vállalható, és a tudásbázisban maradhat.

**Nyitva — emberi döntést igényel:** az omnibusz-prezentáció utolsó diáján account
manager neve, közvetlen telefonszáma és e-mail címe szerepel. Publikus marketinganyagból
származó üzleti kapcsolati adat, de három ok miatt mégis kezelni kell:
a repo publikus, a generált válaszban idézhető, és egy PII-kezelésről szóló projektben
rosszul mutat. **Javaslat:** az ingest során ez a dia kimarad vagy a kontakt-blokk
maszkolva kerül be; a generált válasz általános kapcsolatfelvételre irányít.
Az érintett kollégával egyeztetni kell.

**Mellékhaszon:** ez egyben a legjobb demó-példa a PII-rétegre — élő, valós eset,
nem kitalált tesztadat.

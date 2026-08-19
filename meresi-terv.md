# Mérési terv

**Rendszer:** NRC kutatástervező asszisztens (ügyfélirányú PoC)
**Adatforrás:** `run_log` tábla a meglévő PostgreSQL adatbázisban
**Utolsó frissítés:** 2026.08.19

---

## 1 / A mérési terv logikája

Három elvet követ, amit a vezetői kör előtt is ki lehet mondani:

**Minden sorhoz létező adatforrás tartozik.** Ahol a PoC ma még nem naplóz,
ott a "Mit kell hozzá beépíteni" oszlop mondja meg, mi hiányzik. Nincs olyan
metrika, aminek az adatforrása "majd megoldjuk".

**A hibát is mérjük, nem csak a sikert.** Négy metrika kifejezetten arra való,
hogy a rendszer gyengeségét mutassa. Ha ezek javulnak, az önmagában siker.

**A megoldott fájdalmakhoz kötött metrikák külön jelölve.** Amit a use case
ígért, azt méri is: a válaszidő az 1-es fájdalomra, az agenttel lezárt arány
a 2-esre, a lefedett ügyfélkör az 5-ösre, az első válaszig eltelt idő a 7-esre.

---

## 2 / A tábla

| # | Mit mérünk | Honnan lesz adat | Hogyan riportáljuk | Kinek | Típus |
|---|---|---|---|---|---|
| 1 | Válaszidő az ügyfél felé | `run_log.latency_ms` | heti automatikus összesítő | folyamatgazda | siker, fájdalom 1 |
| 2 | Agenttel lezárt kérdések aránya | `run_log.outcome` = `answered` / összes | heti összesítő | folyamatgazda | siker, fájdalom 2 |
| 3 | Eszkalációs arány és okok | `run_log.outcome` = `escalated`, `escalation_reason` szerint bontva | heti összesítő | folyamatgazda | **hiba** |
| 4 | Jóváhagyás előtti szerkesztés mértéke | `run_log.edit_distance` | havi egy dia | szponzor | **hiba** |
| 5 | Elutasított javaslatok aránya | `run_log.approval_status` = `rejected` | havi egy dia | szponzor | **hiba** |
| 6 | Jóváhagyásig eltelt idő | `run_log.approved_at` − `created_at` | heti összesítő | folyamatgazda | siker, fájdalom 7 |
| 7 | Kérdésenkénti modellköltség | `run_log.cost_usd` — **ma nem töltött** | havi összesítő | szponzor | költség |
| 8 | Kiszolgált ügyfelek száma és mérete | `run_log.session_id` + CRM-összekötés | havi egy dia | szponzor | siker, fájdalom 5 |
| 9 | Ismétlődő kérdéstémák | `run_log.question_masked` havi kézi kódolás | negyedéves elemzés | folyamatgazda | tanulás, fájdalom 6 |
| 10 | PII-találatok száma | PII-szűrő számlálója | heti összesítő | IT-biztonság | **hiba** |
| 11 | Retrieval-minőség a golden seten | `threshold_results.csv` újrafuttatva | havonta, kiadás előtt | fejlesztés | **hiba** |
| 12 | Munkaidőn kívüli kérdések aránya | `run_log.created_at` időbélyeg | havi egy dia | szponzor | siker, fájdalom 1 |

---

## 3 / Amit ma még nem naplóz a PoC

| Metrika | Mi hiányzik | Becsült munka |
|---|---|---|
| 7 — modellköltség | a `cost_usd` mező létezik, de üresen marad: a pipeline függvényei nem adják vissza a token-számokat, ezért a HyDE, embedding, rerank és generálás hívásait kellene kiegészíteni usage-visszaadással | 3-4 óra |
| 8 — ügyfélkör | nincs ügyfélazonosító a `run_log`-ban; CRM-összekötés és jogosultsági modell kell | 2-3 nap |
| 9 — kérdéstémák | a kézi kódolás nem skálázódik; automatikus témacímkézés kellene | 1 nap |
| 10 — PII-találatok | a szűrő maszkol, de nem számlál; számláló-mező kell a `run_log`-ba | 2 óra |
| 12 — munkaidőn kívüli arány | az időbélyeg megvan, de nincs munkaidő-definíció a riportban | 1 óra |

A többi nyolc metrika a PoC jelenlegi naplózásából számolható.

---

## 4 / Baseline — amihez mérünk

Baseline nélkül nincs business case. A jelenlegi állapot **nincs mérve**,
ezért a pilot első két hete egyben baseline-mérés is.

| Mit mérünk | Mai érték | Mért vagy becsült | Forrás |
|---|---|---|---|
| Módszertani megkeresések száma | nincs adat | — | két hét mérés kell |
| Első válaszig eltelt idő | 1 munkanap (ajánlat) | **ökölszám** | nrcdata.hu vállalás |
| Kutatói idő megkeresésenként | nincs adat | — | két hét mérés kell |
| Ajánlatkéréstől ajánlatig | 5-7 munkanap | **becsült** | omnibusz termékleírás |

Ez a tábla szándékosan hiányos. A brief kimondja: ha egyik sorhoz sincs forrás,
a következő lépés nem fejlesztés, hanem két hét mérés. A pilot ezt oldja meg.

---

## 5 / Küszöbök, amiknél beavatkozunk

| Metrika | Küszöb | Mi történik, ha átlépi |
|---|---|---|
| Eszkalációs arány | > 40% | a tudásbázis hiányos, ingest-kör kell |
| `edit_distance` átlaga | > 30% | a generálás minősége nem elég, prompt-iteráció |
| Elutasítási arány | > 10% | a rendszer rossz javaslatokat ad, pilot leállítása mérlegelendő |
| Retrieval golden set | bármely A-kategóriás kérdés 0.3 alá esik | regresszió, kiadás visszatartva |

---

## 6 / Mért adat a PoC-ból — retrieval-minőség

A 12-es metrika első mérése megtörtént, 24 kérdéses kalibrációs készleten,
két körben. **Mért adat, nem becslés.**

| Kategória | avg score (v1) | avg score (v2) | max score (v2) |
|---|---|---|---|
| A / erős pozitív | 0.557 | 0.666 | 1.000 |
| B / gyenge pozitív | 0.551 | 0.640 | 0.999 |
| C / negatív | 0.165 | 0.053 | 0.108 |
| D / szabály alapú eszkaláció | 0.061 | 0.002 | 0.004 |

A v1 és v2 között két beavatkozás történt: a HyDE-prompt fogalmi kontextussal
bővült, és a tudásbázisból kiszűrtük a CMS-fejlesztési tartalmat.

**Amit ez jelent:** a negatív kérdések maximuma 0.53-ról 0.11-re esett, tehát
az a sáv, amin belül biztonságosan lehet eszkalálni, kilencszeresére nőtt.
Az eszkalációs küszöb ezért **0.3**, mért alapon, nem becsléssel.

**Amit ez nem jelent:** a rendszer nem hibátlan. Két A-kategóriás ténykérdés
(kérdőív-leadási határidő, mennyiségi kedvezmény) a küszöb alatt maradt, tehát
ezekre ma eszkalál, pedig a válasz a tudásbázisban van. Ez hamis negatív:
kényelmetlen, de nem veszélyes. A fordítottja — magabiztos rossz válasz —
lenne a veszélyes, és abból a mérés egyet sem mutatott.

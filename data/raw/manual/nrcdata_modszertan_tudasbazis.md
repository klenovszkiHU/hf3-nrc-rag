# NRC Módszertani Tudásbázis: 15 piackutatási módszer szakmai leírása

## TL;DR
- Ez az anyag 15 kvantitatív és kvalitatív módszer ajánlatkész, szakmailag hiteles leírását adja — definíció, mikor (nem) alkalmazzuk, mintavétel, projektstruktúra, output, korlátok, benchmarkok és a hasonló módszerek megkülönböztetése.
- A legfontosabb döntési elvek: az ármódszereknél a Van Westendorp az elfogadható ártartományt, a Gabor-Granger a bevételmaximáló pontot adja; a választásmodelleknél a CBC a piaci szimuláció alapmódszere, az ACBC kisebb mintán is stabil; a szegmentációnál mindig több klaszterszám-kritériumot kell ütköztetni.
- A módszertani hitelesség kulcsa a limitációk explicit kezelése: az online panel nem valószínűségi minta (súlyozás kötelező), az NPS prediktív ereje vitatott, a Nielsen-féle 5-fő szabály csak kvalitatív feltárásra igaz, és az eye-tracking hőtérkép önmagában nem oksági bizonyíték.

## Key Findings

**Kvantitatív adatfelvétel.** A CAWI ma a domináns adatfelvételi mód, de nem valószínűségi minta: a reprezentativitást kvótázással és utólagos súlyozással közelítjük, az adatminőséget pedig speederek, straight-linerek, botok és figyelemellenőrzések szűrésével biztosítjuk. Az ESOMAR/GRBN álláspont szerint egyetlen online panel sem lehet teljes mértékben reprezentatív; ezt az ajánlatban is transzparensen kell kezelni.

**Ármódszerek.** A Van Westendorp négy percepciós kérdésből elfogadható ártartományt ad, de nem kezeli a versenyt és nem becsül keresletet. A Gabor-Granger diszkrét árpontokon mért vásárlási szándékból keresleti/bevételi görbét ad. Egyik sem helyettesíti a conjointot versenykörnyezet modellezésére.

**Választás- és preferenciamodellek.** A CBC a piaci szimuláció ipari alapmódszere; az ACBC kisebb mintán is stabilabb egyéni becslést ad; a Max-Diff a Likert-skálák skálahasználati torzításait kerüli el kényszerített trade-off révén.

**Kvalitatív módszerek.** Az FGD a csoportdinamikát használja ki, de kockázata a groupthink és a domináns résztvevő; az IDI mélységet ad (laddering, means-end); az OBB aszinkron, több adatot és átgondoltabb válaszokat hoz.

**CX és UX.** Az NPS egyszerű és benchmarkolható, de prediktív ereje akadémiailag vitatott (Reichheld vs. Keiningham). A usability-nél az 5-fő szabály csak kvalitatív feltárásra érvényes; kvantitatív méréshez 20–40 fő kell.

## Details

### 1. CAWI (Computer Assisted Web Interview)

**Definíció és elméleti háttér.** Számítógéppel támogatott, önkitöltős online kérdőíves adatfelvétel, ahol a válaszadó saját eszközén tölti ki a kérdőívet. Az adatok valós időben állnak elő, ami gyors terepmunkát és folyamatos monitoringot tesz lehetővé.

**Mikor alkalmazzuk / mikor NEM.** Alkalmas nagymintás, standardizált kvantitatív felvételre, gyors trackingre, vizuális stimulusok tesztelésére. NEM alkalmas offline populációk (pl. idősek, alacsony digitális penetrációjú csoportok) reprezentatív lefedésére, valamint nagyon hosszú vagy komplex, interjúztatói segítséget igénylő kérdőívekre (abandonment és satisficing kockázat).

**Mintavétel és reprezentativitás.** Az online panel nem valószínűségi minta. A reprezentativitást kvótás mintavétellel (census-alapú kvótatáblák) és utólagos súlyozással (post-hoc weighting: kor, nem, régió, iskolázottság szerint, rim/raking eljárással) közelítjük. Az ESOMAR/GRBN Online Sample Quality Guideline szerint egyetlen online panel sem garantál teljes reprezentativitást; a súlyozási és projekciós módszereket, valamint a minta populáció-reprezentativitásának értékelését az ISO 20252 / ISO 26362 best practice szerint dokumentálni kell az ügyfél felé.

**Projektstruktúra.** (1) Célcsoport és kvóták definiálása → (2) kérdőívszkript és tesztelés → (3) mintakiküldés (soft launch, majd teljes) → (4) valós idejű monitoring és kvótakezelés → (5) adatminőség-szűrés → (6) súlyozás → (7) elemzés/riport.

**Adatminőség-ellenőrzés.** Speederek (a medián kitöltési idő kevesebb mint egyharmadánál gyorsabbak); straight-linerek (grid-kérdésekben azonos válaszpozíció); botok/csalás (IP-szűrés, digitális ujjlenyomat, honeypot, CAPTCHA, duplikátumszűrés – pl. Imperium RelevantID); attention/trap check (2-3 db egy 15 perces kérdőívben). Fontos: a straight-lining önmagában nem feltétlenül rossz válaszadó (lehet valid egységes vélemény), ezért több jelzőt együtt kell értékelni; a Kantar tapasztalata szerint a grid-ekben a legkárosabb minta inkább a random válasz, mint a straight-lining. Ha a speeder-flag 5% fölé megy, a küszöböt felül kell vizsgálni. Egy UX benchmark-tanulmányban a válaszok közel 18%-át szűrték ki minőségi okból.

**Korlátok.** Fedettségi torzítás (coverage bias), önszelekció, panel-elhasználódás (professzionális válaszadók), mobil eszközön nehezebb speedert azonosítani (a mobil kitöltés 25-50%-kal hosszabb, ezért eszközönként eltérő küszöb ajánlott).

### 2. Omnibusz kutatás

**Definíció.** Több megrendelő kérdéseit egyetlen, rendszeresen (heti/havi) futó kérdőívben egyesítő, megosztott költségű felvétel. A megrendelő általában 3-10 kérdést vásárol, és csak a saját kérdéseinek eredményét kapja meg.

**Mikor érdemes omnibuszt választani ad-hoc helyett.** Kis kérdésszám, gyors és költséghatékony egyszeri "pillanatkép" (awareness, attitűd, penetráció), trendkövetés visszatérő hullámokban. NEM alkalmas: mély, sok kérdést vagy komplex logikát igénylő témára, niche célcsoportra (osztott mintában alacsony esetszám), vagy ha a teljes adatbázis tulajdonjoga kell.

**Osztott minta korlátai.** A megrendelő csak a saját kérdéseit kontrollálja, a mintaszerkezetet és a kérdőív egészét nem. Niche alcsoportoknál az esetszám gyorsan lecsökken. Az omnibusz a bizonytalanság korai csökkentésére való, nem stratégiai mélyelemzésre.

**Kontextuális hatások (context effects).** Más megrendelők megelőző kérdései befolyásolhatják a válaszokat (priming, sorrendhatás). A kérdéssorrend és -kontextus tudatos értelmezése szükséges; jó gyakorlat a saját kérdésblokk elején semleges bevezetés, és a más témájú blokkoktól való elkülönítés kérése a szolgáltatótól.

### 3. Fókuszcsoportos vizsgálat (FGD)

**Definíció.** 5-10 fős, moderátor által vezetett kvalitatív csoportos beszélgetés egy adott témáról, ahol a csoportinterakció maga is adatforrás.

**Moderátor szerepe.** Facilitál, nem vezet. Technikák: a szünet (3-5 mp várakozás a hozzászólás után, hogy más töltse ki a csendet), átirányítás ("Hallgassuk meg azt is, aki másképp látja"), konkretizáló szondázás ("Tudna konkrét példát mondani?"), domináns hangok kezelése ("Szeretném, ha mindenkit hallanánk – X, te hogy látod?").

**Discussion guide felépítése.** Bevezetés/bemelegítés → általános témakörök → fókuszált kérdések → mélyítő szakasz (stimulusok) → lezárás. Tölcsér-elv (általánostól a specifikusig).

**Csoportdinamika kezelése.** Fő veszélyek: dominancia-hatás, groupthink (konszenzuskeresés a valós vélemény rovására), halo-hatás, akvieszcencia, priming, társas kívánatosság (social desirability). A Nielsen Norman Group szerint a groupthink az FGD leggyakoribb hibaforrása. Onwuegbuzie et al. (2009) javaslata a részvételi mintázatok (pl. nem/kor szerinti) Venn-diagramos monitorozása, hogy a moderátor kiegyenlíthesse a hozzászólásokat.

**Homogén vs heterogén csoport.** Homogén: kevesebb gátlás, mélyebb azonosulás; heterogén: több nézőpont, de konfliktus- és dominanciakockázat. Érzékeny témáknál homogén csoport ajánlott.

**Elemzés.** Thematic analysis (pl. Braun & Clarke fázisai), content analysis, grounded theory. Transzkript + moderátori megfigyelési jegyzetek együttes elemzése; konszenzus, nézeteltérés és meglepetés azonosítása, a non-verbális reakciók (kényelmetlenség, lelkesedés, zavar) rögzítése.

### 4. Mélyinterjú (IDI)

**Típusok.** Strukturált (fix kérdéssor), félig strukturált (guide + rugalmas szondázás – a leggyakoribb), narratív (a válaszadó saját elbeszélése vezet).

**Laddering technika.** A means-end chain (MEC) elméleten alapul (Gutman 1982; Reynolds & Gutman 1988; gyökerei Kelly személyes konstrukció-elméletében és Bannister & Mair 1968 munkájában). Az ismételt "Miért fontos ez Önnek?" kérdéssel az attribútumoktól (A) a következményeken (C) át az értékekig (V) jutunk. Soft laddering (nyílt, félig strukturált interjú – az eredeti és leggyakoribb) vs. hard laddering (strukturált protokoll, AI-moderálásra és kezdő interjúztatókra is alkalmasabb). Output: implikációs mátrix (közvetlen/közvetett kapcsolatok gyakorisága) és Hierarchical Value Map (HVM).

**Elicitation technikák.** Triádok (Kelly-repertory grid), képek/prototípusok bemutatása, projektív technikák. Az elicitáció jellemzően 3-6 attribútumot hoz felszínre résztvevőnként, mindegyik egy-egy ladder alapja.

**Elemzés és mintaméret.** Priorizált szegmensenként 15-30 fő; B2B-ben kevesebb is elég a mélység miatt. Transzkript-kódolás intercoder reliability ellenőrzéssel (több kódoló). Buktató: a "miért" robotikus ismétlése kihallgatássá válik; a valóságban az attribútumok gyakran több következményhez/értékhez kapcsolódnak (fa-szerkezet, nem lineáris lánc).

### 5. Online Bulletin Board (OBB) / Aszinkron online kvalitatív

**Definíció.** Aszinkron, digitális platformon zajló kvalitatív kutatás, ahol a résztvevők saját időben, több napon át (jellemzően napi ~30 perc, 2-3 napon keresztül) válaszolnak feladatokra.

**Előnyök.** Rugalmasság (időzóna, elfoglaltság független); átgondoltabb, mélyebb válaszok (nem "top-of-mind"); sokkal több adat (akár 10x a live FGD-hez képest, mert mindenki minden moderátori kérdésre válaszol); nagyobb csoportméret (20-30, akár 100 fő); képi/videós feladatok könnyű beépítése; kvantifikált "quick poll" kérdések (pl. "melyik dizájn tetszik jobban?") irányadó konszenzushoz.

**Hátrányok.** Nehezebb bizalmat/rapportot építeni, nincs valós idejű non-verbális jelzés; nagy adatmennyiség elemzési terhe (a platformok tag/sort/kategorizálás eszközökkel segítenek); moderátori elköteleződés több napon át.

**Moderálási technikák.** Ütemezett kérdésmegjelenítés (egyszerre / lépcsőzetesen / adott napszakban), egyéni szondázó prompts, média-stimulusok, group segmentation (elágazás demográfia/válasz alapján), automatikus emlékeztetők (e-mail/SMS/push). Alapelv: engaging, fejlődő élmény legyen, ne Q&A stílusú (utóbbi a kvanthoz illik).

### 6. Koncepciótesztelés

**Dizájnok.** Monadic (minden válaszadó 1 koncepciót lát – legtisztább, valós életet szimulál, normadatbázis-kompatibilis, de nagyobb minta kell); sequential monadic (több koncepció, randomizált sorrend – olcsóbb, kisebb minta, de **suppression effect**: minden score szisztematikusan alacsonyabb, mert az első koncepció referenciaponttá válik, és **interaction effect**: egy kiemelkedő termék aránytalanul lehúzza a többit); paired comparison (közvetlen összehasonlítás – nem normakompatibilis, erős interaction effect); protomonadic (monadic + záró páros összehasonlítás mint "safety net", jellemzően central location taste testben).

**Kritikus figyelmeztetés:** a sequential monadic eredmények a suppression effect miatt NEM hasonlíthatók közvetlenül a pure monadic normákhoz; korrekciós faktor vagy egyidejűleg futtatott monadic kontrollcella szükséges.

**Mérőeszközök.** Relevance, uniqueness, believability, purchase intent (5-fokú: definitely/probably would buy…). A "legjobb koncepció" kiválasztásához külön "correct selection" statisztikai eljárás használatos (nem az összes pár szignifikancia-tesztje).

**BASES modell.** A Nielsen BASES (eredetileg Booz-Allen Sales Estimating System; Lynn Y.S. Lin, Burke Marketing Research, 1977; Nielsen-akvizíció 1998) szimulált tesztpiaci (STM) modell, amely a fogyasztói válaszokat "leszállítja" (deflálja) a túlbecslés korrigálására, majd a marketingtervekkel (bevezetés, budget, disztribúció, reklám/promóció, szezonalitás) kombinálva kétéves volumenelőrejelzést ad (trial + repeat). Alapelv (Ashok Charan, MarketingMind, NUS): "Consumers do not usually do what they claim to do… While consumers overstate their intended purchase behaviour, they tend to do so with consistency", és a túlbecslés mértéke országonként/kultúránként/mérésenként eltér. A norma-adatbázis mérete Charan (MarketingMind) szerint "about 300,000+ concept tests and 500,000+ forecast (as of 2021)", amelyből a korrekciós faktorok és benchmarkok származnak; a NielsenIQ programja 40+ éves, 80+ piacot fed le. Fontos nüansz: a koncepció-fázisú purchase intent gyengébb prediktor, mint az after-use intent (utóbbi erősen korrelál a piaci sikerrel), ezért a sikerküszöböket elsősorban az after-use score-okból vezetik le. A pontos deflációs együtthatók (a "definitely" vs. "probably would buy" kalibrációja) a Nielsen üzleti titkai, nyilvánosan nem közöltek.

**Normadatbázis szerepe.** Az abszolút score-ok önmagukban nem értelmezhetők; a kategória-normákhoz viszonyítás (pl. top-two-box vs. weighted purchase intent) adja a jelentést. A BASES a saját teljes adatbázisához hasonlít, nem versenytárs-koncepciókhoz.

### 7. Csomagolásdizájn teszt (Pack Test)

**Tachistoszkóp módszer.** Rövid, kontrollált idejű (pl. 50 ms-tól felfelé) expozíció, amely a polcon való gyors észlelhetőséget (findability, standout) méri. Elméleti alapja a vizuális észlelés-kutatás (Loftus 1981 tachistoszkópos fixáció-szimulációi, korneális reflexió-alapú eye-tracking rendszerrel, ±0,5° pontossággal).

**Shelf simulation.** Valós vagy virtuális (VR) polckörnyezet, ahol mérjük: mely terméket veszik észre először, keresési mintázatok, találási idő.

**First Moment of Truth (FMOT).** A polc előtti néhány másodperc, amikor a vásárló dönt – a csomagolásnak itt kell kitűnnie. A viselkedés-alapú (nem self-report) csomagoláskutatás erősen korrelál a piaci teljesítménnyel, bár egyetlen módszer sem jelzi tökéletesen az eladásokat.

**Eye-tracking kombináció.** Webkamerás vagy szemüveges eye-tracking a fixációk számával/időtartamával, plusz reakcióidő-mérés az implicit attitűdökhöz. Egy publikált vizsgálatban 6 csomagolásstílust (AOI1-6) teszteltek Tobii Pro Glasses 3-mal; a függőleges logós, realisztikus képű variáns kapta a legtöbb figyelmet, és az ANOVA szignifikáns különbséget mutatott (p < .001); a szimulált polc középső pozíciója kapta a legtöbb figyelmet.

### 8. Reklámpre-teszt

**Diagnosztikai mutatók.** Attention (figyelem/intrusiveness), branding (márkakötés/recognition), communication (üzenetátadás/megértés/recall), motivation (persuasion/purchase intent). A jó gyakorlat több mutató kompozit értelmezése, nem egyetlen szám: az iparági norma szerint a persuasion mellett recall/intrusiveness, communication, imagery és likeability mérőszámokat is használnak.

**Copy testing modellek.** Ipsos ASI (Next*TV: otthoni expozíció 30 perces TV-műsorba ágyazva "műsorkutatás" álcával, day-after-recall telefonos visszahívással + forced exposure diagnosztika; pre-post purchase intent maszkolt kérdéssel); Millward Brown Link (1989 óta, ~240 000 tesztelt reklám; a nevét Gordon Brown 1987-es "The Link between Sales Effects and Advertising Content" tanulmányából kapta; facial coding és eye-tracking integrálva). Módszertani vita: az Ipsos szerint a márkát az első másodpercekben mutatni kell, a Millward Brown szerint nem feltétlenül.

**Normadatbázis szerepe.** A score-okat kategória-normákhoz viszonyítják. Kritikák: (1) a facial coding prediktív ereje reklámra alacsony (egy Nielsen/CBS-vizsgálatban ~9%, a survey alatt); (2) az egyszeri kvantitatív "score" nem mondja meg, hogyan javítsunk – erre a kvalitatív pre-teszt informatívabb. Best practice: kvant validáció + kvalitatív diagnosztika kombinálása.

### 9. Van Westendorp Price Sensitivity Meter (PSM)

**Elmélet.** Van Westendorp, P. (1976), "NSS-Price Sensitivity Meter (PSM) – A new approach to study consumer perception of price", Proceedings of the 29th ESOMAR Congress (Velence), 139–167. Négy nyílt kérdés: too cheap (kételkedik a minőségben), cheap/bargain, expensive (de még megfontolja), too expensive (nem venné meg). Feltevés: a válaszadó képes elképzelni az árlandscape-et, és az ár értékjelző.

**Output.** Kumulatív görbék metszéspontjai: PMC (Point of Marginal Cheapness, alsó határ: too cheap × expensive), PME (Point of Marginal Expensiveness, felső határ: too expensive × cheap), OPP (Optimal Price Point: too cheap × too expensive metszés), IPP (Indifference Price Point: cheap × expensive metszés, jellemzően a medián/piaci ár). Range of Acceptable Prices = PMC–PME. Newton-Miller-Smith kiterjesztés (Newton, D., Miller, J., Smith, P., 1993, AMA Advanced Research Techniques Forum): purchase intent kérdésekkel közelítő keresletbecslés.

**Korlátok / mikor NEM.** Nem veszi figyelembe a versenyt (kompetitív vákuum); a vonal-metszéses megközelítést gyenge elméleti alapon kritizálják ("largely been criticized and discredited as lacking good theory"); nem becsül bevételt/keresletet. NEM alkalmazzuk, ha a versenykörnyezet vagy a bevételmaximálás a kérdés (akkor Gabor-Granger vagy conjoint). A kérdésmegfogalmazás és -sorrend érzékenyen befolyásolja az eredményt (dokumentált esetben eltérő megfogalmazás 27%-os árkülönbséget okozott); kérdésrandomizálás ajánlott az anchoring ellen.

**Minta.** Legalább 100 komplett válasz; szegmensenként külön ez a küszöb. Széles árvalidációs tartomány ajánlott (min. 0-tól).

### 10. Conjoint elemzés

**Típusok.** CBC (Choice-Based Conjoint): választás alternatívák közül, a piaci szimuláció ipari alapmódszere, aggregált szinten erős, valós vásárlási helyzetet szimulál. ACA (Adaptive Conjoint Analysis): adaptív, sok attribútumnál, kisebb mintánál. ACBC (Adaptive CBC): BYO (build-your-own) + screener (must-have/unacceptable) + tournament szakasz; egyéni szinten stabilabb kisebb mintán, engedélyezőbb és realisztikusabb interjúélmény (a hosszabb interjú ellenére a válaszadók jobban preferálják).

**Part-worth értelmezés.** A part-worth utility interval-skálájú, attribútumon belül önkényes additív konstanssal (effects coding: attribútumon belül 0-ra összegződik). Csak attribútumon belül hasonlítható, attribútumok között NEM (pl. egy negatív utility nem jelenti, hogy a szint nem vonzó). Az attribútum-fontosság a utility-range aránya (%, ratio-skála, 100%-ra összegződik), de a random hiba felfelé torzíthatja – ezért heterogén preferenciáknál latent class vagy HB (hierarchikus Bayes) becslés és market simulator/sensitivity analysis ajánlott.

**Market simulator.** Az utility-kből becsli, hogy adott termékkonfigurációkat a válaszadók hány %-a preferálná (share of preference), plusz source of volume és kannibalizáció. Nem-kutatóknak ez a legjobb kommunikációs eszköz (a part-worth magyarázata gyakran félreviszi a menedzsment-prezentációt).

**Mintaméret.** Sawtooth ökölszabály: ~300 fő általános küszöb; jelentendő alcsoportonként +200 fő; CBC-nél 500 expozíció/level a minimum, biztonságosan inkább 1000/level. Az ACBC kis mintán (akár néhány tucat, extrém esetben egyetlen döntéshozó) is stabilizál egyéni utility-t.

### 11. Max-Diff (Maximum Difference Scaling)

**Elmélet.** Best-worst scaling (BWS); Louviere (1991) fejlesztette Thurstone összehasonlító ítélet elméletére (Thurstone-skála, 1927) építve. A válaszadó minden setben (jellemzően 4-6 tétel) a legjobbat és legrosszabbat választja; minden választás két információt ad (pozitív preferencia a "best"-re, negatív a "worst"-re).

**Mikor jobb mint Likert.** Kényszerített trade-off → jobb diszkrimináció a tételek között (a Likertnél minden "fontos" köré tömörül); kikerüli a skálahasználati torzítást (scale use bias) és az akvieszcenciát; kultúrközi összehasonlításra jobb. Hátrány: kognitív teher (fáradás, satisficing kockázat, ha sok a set); nem ad abszolút szintet, csak relatív fontosságot/preferenciát.

**Minta.** Minden tételnek többször kell megjelennie a setek között a stabil becsléshez; jellemzően 20-100 tétel, aggregált elemzéshez 300+ fő (a conjoint-hoz hasonló ökölszabályok szerint).

### 12. Klaszteranalízis / Szegmentáció

**K-means vs hierarchikus.** K-means: előre megadott klaszterszám (K), gyors, nagy mintára, centroid-alapú; hierarchikus (agglomeratív, AHC): dendrogram, nem kell előre K, jobb betekintést ad a klaszterek összeolvadásába, de számításigényesebb. A választás az üzleti kérdéstől függ; gyakori a kettő kombinálása (hierarchikus a K meghatározására, majd k-means a végső hozzárendelésre).

**Optimális klaszterszám.** Elbow method (WCSS/within-cluster sum of squares törése – néha kétértelmű); silhouette score (-1..+1, kohézió vs. szeparáció); gap statistic; Dunn-index; több mint 30 index (NbClust "majority rule"). Best practice: több kritérium együttes használata + üzleti értelmezhetőség, mivel az elbow és a silhouette gyakran eltérő K-t ad ugyanazon adaton.

**Profilozó változók.** A klaszterképző (basis) változók (attitűd, igény, viselkedés) mellett külön profilozó (descriptor) változók (demográfia, médiafogyasztás) írják le és teszik megcélozhatóvá a szegmenseket.

**Validáció.** Stabilitás (split-half, ismételt futtatás eltérő seeddel/random sorrenddel), reprodukálhatóság, diszkriminancia-elemzés, üzleti megkülönböztethetőség, méret és megcélozhatóság (targetability).

### 13. NPS (Net Promoter Score)

**Számítás.** 0-10 "mennyire ajánlaná" kérdés. Promoterek (9-10) % mínusz Detraktorok (0-6) %; a Passzívak (7-8) kimaradnak. Forrás: Reichheld, F. F. (2003), "The One Number You Need to Grow", Harvard Business Review, december, 81(12):46–54 — "The best predictor of top-line growth can usually be captured in a single survey question: Would you recommend this company to a friend?" (14 esettanulmányból 11-ben volt a 'would recommend' a legjobb/második legjobb prediktor). Az NPS bejegyzett védjegy (Reichheld / Bain & Company / Satmetrix).

**Driver analysis.** Top-box analysis vs. regresszió (Key Driver Analysis: többszörös lineáris regresszió; vagy ordered logit/ordered logistic regresszió az NPS-válasz becslésére, amely megadja a hatás erősségét és irányát). A driverek megmondják, mely CX-elemek mozgatják a score-t. Verbatim/nyílt kérdés + (AI) szövegelemzés a "miért" feltárására.

**Closed-loop feedback.** Detraktorokkal (majd promoterekkel) való strukturált visszacsatolás; a hurok lezárása a program lényege, nem a score maga. Transaction NPS (interakció után) vs. relationship NPS (általános). A closed-loop a méréséből retenciós programot csinál.

**Korlátok és kritikák (Reichheld vs Keiningham vita).** Keiningham, Cooil, Andreassen & Aksoy (2007), "A Longitudinal Examination of Net Promoter and Firm Revenue Growth", Journal of Marketing 71(3):39–51 (21 cég, 15 500+ interjú a Norwegian Customer Satisfaction Barometerből; MSI/H. Paul Root Award) nem tudta replikálni Reichheld állítását az NPS "clear superiority"-jéről: az NPS nem jelezte szignifikánsan jobban a bevételnövekedést, mint más metrikák. További kritikák: a 11-fokú skála és a promoter/detraktor vágás önkényes, alacsonyabb prediktív validitással (Schneider et al. 2008); kompozit (több kérdéses) indexek jobbak; a vágások kultúránként eltérnek (Japánban egy 7-es már erős dicséret). Egy 2021-es longitudinális vizsgálat (sportswear iparág) szerint csak a "brand health" NPS (összes potenciális vásárló mintája) jelzi a jövőbeni értékesítést, a klasszikus tranzakciós NPS nem. A vágás diszkontinuitása (10 vevő 6-ról 7-re mozdulása 10 pontot mozgat) kis mintáknál manipulálhatóvá és instabillá teszi. A benchmarkok (Bain, Satmetrix, NICE) csak iparági kontextusban értelmezhetők: +30 kiváló lehet telekomban, de közepes prémium autóban.

### 14. Usability teszt

**Think-aloud.** A felhasználó hangosan verbalizálja gondolatait feladatvégzés közben (Ericsson & Simon 1993). Elakadásnál: "Mire gondol most?" A formatív think-aloud enyhíti a self-report kognitív torzításait, mert a kutató látja, mit tesz a felhasználó, nemcsak amit mond.

**Moderált vs moderálatlan.** Moderált (mély, szondázható, drágább) vs. moderálatlan (skálázható, olcsó, gyors, de nincs követő kérdés). Best practice a formatív (feltáró) és szummatív (mérő) megközelítés kombinálása.

**Mintaméret – Nielsen 5-fő szabály és kritikája.** Nielsen, J. & Landauer, T. K. (1993), "A Mathematical Model of the Finding of Usability Problems", Proceedings of ACM INTERCHI'93 (Amszterdam, ápr. 24–29), 206–213. Képlet: N(1-(1-L)^n); az NN/G szerint "The typical value of L is 31%, averaged across a large number of projects we studied", és L=0,31 mellett n=log(0,15)/log(0,69)≈4,7 → 5 fő tárja fel a problémák ~85%-át. Nielsen érve: 3×5 fő (iteratív) jobb, mint 1×15 fő. Kritika: csak kvalitatív feltárásra és homogén felhasználói csoportra igaz; Spool & Schroeder (2001) szerint a mintaméret a probléma-sűrűségtől függ, nem általánosítható 5-re; több felhasználói szegmensnél szegmensenként 5 kell. Kvantitatív mérésre (task success rate, SUS benchmark) 20-40 fő kell (90%-os konfidenciaszinten); alacsony gyakoriságú (10-20% felfedezési rátájú) hibákhoz 9-18 fő. Iparági benchmark: a >78%-os task-completion rate átlag feletti, sok csapat ~80%-ot vár launch előtt.

**SUS (System Usability Scale).** Brooke (1996), 10 tétel, váltakozó pozitív/negatív megfogalmazás, 0-100 skálára konvertálva (×2,5). Sauro & Lewis (2016; Sauro 2011) 446 tanulmány / 5000+ SUS-válasz alapján: átlag 68, szórás 12,5 — "A SUS score above a 68 would be considered above average and anything below 68 is below average"; az "A" (kiváló) küszöb 80,3 felett (felső 10%), az "F" 51 alatt. Figyelmeztetés: a SUS "quick and dirty" mérőszám, a válaszok mögötti racionalizáció zajt vihet be (negatív ferdeség), ezért érdemes think-aloud-dal kiegészíteni.

### 15. Szemkamerás vizsgálat (Eye-tracking)

**Alapmetrikák.** Fixáció (a tekintet stabil megállása, ~100-300 ms; a <300 ms alatti gyakran nem kódolódik memóriába, a gyakorlati eszközök ~100 ms-tól rögzítenek); szakkád (gyors szemmozgás fixációk között); regresszió/visszatérés (observation count – hányszor tér vissza egy AOI-ra); time to first fixation; total fixation duration; first-fixation duration. A gaze point az alapegység (60 Hz-es eszköz 60 gaze pontot rögzít másodpercenként).

**AOI (Area of Interest) elemzés.** Előre definiált régiók (logó, ár, üzenet, gomb), amelyekre a metrikákat számoljuk. Point-based (raw gaze/scanpath, szemantikai annotáció nélkül) vs. AOI-based (szemantikus, régiók közti átmenetek) vizualizáció.

**Hőtérkép értelmezés.** A "heat intensity" = az AOI-t fixálók aránya × átlagos fixációs idő. Meleg színek (piros/sárga) = hosszabb/gyakoribb nézés. Óvatosan: a hőtérkép aggregátum, nem oksági bizonyíték; a hosszú fixáció lehet érdeklődés VAGY zavar (nem egyértelmű, hogy az AOI vonzó vagy zavaró). A hosszú time-to-first-fixation (>0,15 mp) jelezheti a rossz pozicionálást.

**Statisztikai megbízhatóság.** A fixáció/szakkád klasszifikációs algoritmus (fixation filter) megválasztása szignifikánsan befolyásolja az eredményt, és a gyártók gyakran nem közlik a pontos számítást; a kalibráció minősége kritikus (különösen speciális populációknál – gyerekek, neurodivergens csoportok – ahol jelvesztés, mozgás rontja az adatminőséget); kombinálni kell más módszerrel (survey, think-aloud, click rate). A kis minta, a publikálatlan algoritmusok és a kontextus nélküli értelmezés a fő validitási kockázatok.

## Hasonló módszerek megkülönböztetése

- **FGD vs IDI:** csoportdinamika és interakció vs. egyéni mélység; érzékeny/normatív vagy erősen egyéni döntési témánál IDI (nincs groupthink, nincs társas kívánatosság), társas/interaktív jelenségnél FGD.
- **Conjoint vs Max-Diff:** conjoint = többattribútumos termék trade-off, piaci szimuláció, share-becslés; Max-Diff = tételek/feature-ök/üzenetek relatív prioritása egyetlen dimenzió mentén (nincs "termék", nincs ár-trade-off).
- **Van Westendorp vs Gabor-Granger:** VW = elfogadható ártartomány percepcióból, amikor még nem tudjuk, milyen ársáv reális, és inkább kategória/új termék a tét; GG = keresleti/bevételi görbe és bevételmaximáló pont diszkrét árpontokból, amikor ismerjük a sávot és egy konkrét termék optimális árát keressük. Illusztratív esetben (Conjointly, instant kávé) a VW elfogadható sávja $5,75–$7,67 volt, míg a GG bevételmaximáló pontja $13,89 — a két módszer más kérdésre válaszol, és nagyon eltérő számot adhat. Kulcskorlát (Quali-Fi): a VW feltételezi, hogy a válaszadó dollárban ki tudja fejezni a percepcióit (kategóriaismeret kell); a GG összeomlik, ha a tesztelt árak mind túl magasak (mindenki nemet mond) vagy túl alacsonyak (mindenki igent). Egyik sem modellez versenyt/bundling-ot – arra conjoint kell.
- **CBC vs ACBC:** CBC statikus, aggregált szintű piaci szimulációra optimális; ACBC adaptív, egyéni szinten kis mintán is stabil, és a must-have/unacceptable szűrővel feltárja a nem alkudható attribútumokat.
- **Monadic vs sequential monadic:** tiszta, valós életet szimuláló, normakompatibilis, de drágább (nagyobb minta) vs. olcsóbb, kisebb minta, de suppression és interaction effect terheli, és nem hasonlítható monadic normákhoz.

## Recommendations

1. **Ajánlatkészítéskor mindig a döntési kérdésből induljunk ki, ne a módszerből.** Ártartomány feltárása → Van Westendorp; egy konkrét termék bevételmaximáló ára → Gabor-Granger; versenyben lévő termékportfólió és feature/ár trade-off → conjoint (CBC).
2. **CAWI-ajánlatban transzparensen jelezzük a reprezentativitás korlátait** (nem valószínűségi minta) és a súlyozási tervet (kvóták + rim weighting); építsünk be dokumentált adatminőség-protokollt (speeder/straight-liner/attention/bot check), és a záró riportban jelentsük a kiszűrt esetek arányát.
3. **Koncepció- és reklámteszteknél kössük ki a normadatbázis-hivatkozást és a dizájnt** (monadic ajánlott, ha összehasonlítás normákkal a cél); sequential monadicnál explicit jelezzük a suppression effect korlátját és a korrekció módját.
4. **NPS-projektnél soha ne álljunk meg a score-nál:** driver analysis (regresszió) + verbatim-elemzés + closed-loop legyen a csomag, és az ajánlatban jelezzük az NPS prediktív korlátait (Keiningham 2007), iparági-kontextusú benchmarkkal, valamint az önmagában vett score volatilitását kis mintán.
5. **Usability-ajánlatnál különítsük el a kvalitatív (5-8 fő/szegmens, iteratív, ~85% problémafeltárás) és a kvantitatív (20-40 fő, SUS/task success, konfidenciaintervallum) célt** — ne ígérjünk statisztikai szignifikanciát 5 főből.
6. **Szegmentációnál kössük ki, hogy több klaszterszám-kritériumot ütköztetünk** (elbow + silhouette + üzleti értelmezhetőség) és stabilitás-validációt végzünk; a szegmenseket profilozó változókkal tegyük megcélozhatóvá.
7. **Küszöbök, amelyek módosítják az ajánlást:** ha a célcsoport erősen offline (pl. 65+, alacsony digitális penetráció) → CAWI helyett/mellett CATI/CAPI; ha a niche alcsoport esetszáma omnibuszban <100 → ad-hoc; ha a conjoint alcsoportos elemzést kér → minta +200/alcsoport; ha az árkutatásnál a verseny a fő tényező → VW/GG helyett conjoint.

## Caveats

- Több forrás (surveyszoftver-gyártók, kutatócégek blogjai) marketingérdekelt; a benchmarkszámok (pl. BASES 41%/81% top-two-box illusztratív példaérték, NPS iparági sávok, VW $5,75–$7,67 vs. $13,89 egyetlen Conjointly-esettanulmányból) illusztratívak, NEM univerzális normák — az ajánlatban is így kell prezentálni őket.
- A BASES pontos kalibrációs/deflációs együtthatói proprietárisak; a nyilvános források csak a deflációs logikát és a normadatbázis-alapú benchmarkolást erősítik meg, a konkrét szorzókat nem.
- A magyar kontextus-források nagyrészt önbevallásosak: az NRC (Net Research Center, alapítva 1999, ügyvezető Klenovszki János) Netpanel.hu panelmérete forrástól/dátumtól függően 120 000–150 000 validált tag, és a cég "öt szempont szerint reprezentatív" mintákat hirdet. Fontos megkülönböztetés: az MMSZ a Magyar Marketing Szövetség (marketing-, nem piackutató-szakmai szervezet), míg a piackutató-szakmai szövetségre az MRSZ acronym használatos; az NRC saját tagságlistája szerint "ESOMAR | MMSZ | MRSZ | IAB Hungary" tag. A magyar reprezentativitási standardokra a legmérvadóbb intézményi forrás a KSH 2020-as, reprezentatív mintavételről szóló ajánlása, amely kifejezetten hivatkozik az ESOMAR-ajánlásokra; megjegyzendő azonban, hogy a klasszikus ESOMAR 10-tételes tartós-cikk lista státuszmérésre Magyarországon elavultnak bizonyult (Szegedi Egyetem / OTKA K 67803). (Ezek a magyar adatok a kutatási keret kimerülése miatt részben másodlagos/önbevallásos forrásokból származnak, és külön ellenőrzést érdemelnek publikálás előtt.)
- Egyes állítások jövőbeli/prediktív jellegűek (pl. NPS mint "early warning system", amely "several quarters"-rel megelőzi a bevételcsökkenést); ezeket nem bizonyított tényként, hanem szolgáltatói hipotézisként kezeljük.
- A klasszikus szakirodalmi hivatkozások (Gutman 1982, Reynolds & Gutman 1988, Louviere 1991, Thurstone 1927, Brooke 1996, Ericsson & Simon 1993) másodlagos összefoglalókból származnak; primer publikáció előtt érdemes az eredeti forrásokat visszaellenőrizni.
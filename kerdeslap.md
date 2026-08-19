# Kérdéslap

Felkészülés a vezetői kör kérdéseire. Minden válasz a saját PoC-ra mutat,
nem általánosságokra.

---

## 1 / Milyen személyes adat kerül a rendszerbe, és melyik pontján tűnik el?

A rendszer tervezés szerint nem kér és nem tárol személyes adatot: az ügyfél
üzleti kérdést ír le, nem személyeset. Mivel azonban szabad szöveges beviteli
mezőről van szó, a gyakorlatban bármi bekerülhet — aláírás, telefonszám,
kollégák neve. Ezért a kérdés a pipeline hívása **előtt** áthalad egy regex-alapú
PII-szűrőn (`src/client/pii.py`), ami e-mail címet, magyar telefonszámformátumokat,
adószámot, adóazonosító jelet, TAJ-számot és bankszámlaszámot maszkol
pszeudonimizálással; a maszkolt token a válaszban visszahelyettesítődik, tehát
a modell soha nem látja az eredeti értéket, az ügyfél mégis normális választ kap.
A `run_log` táblába kizárólag a maszkolt kérdésszöveg kerül. Fontos korlát,
amit nem hallgatunk el: a magyar nyelvű PII-detektálás recallja tipikusan gyenge,
a regex magas precisionnel de alacsony fedéssel dolgozik, ezért ez egy réteg
a négyből — adatosztályozás, hozzáférés-kontroll, PII-szűrő, szolgáltatói
szerződés —, nem önálló védelem.

## 2 / Hol fut a modell, hova utazik az adat, mi nem hagyja el a környezetünket?

A rendszer három külső szolgáltatót hív egyetlen kérdés kiszolgálása során,
és ezt az adattérkép dia teljes egészében ábrázolja. Az OpenAI
`text-embedding-3-small` kapja a HyDE-hipotézist embeddinghez, a Cohere
`rerank-multilingual-v3.0` kapja a kérdést és a jelölt szövegrészleteket
újrarendezéshez, az Anthropic Claude pedig a hipotézisgenerálást (Haiku) és
a válaszgenerálást (Sonnet) végzi. Mindhárom szolgáltató az Európai Unión
kívül, elsősorban az Egyesült Államokban működtet infrastruktúrát, tehát
harmadik országba történő adattovábbításról van szó, amit szerződéses
garanciákkal kell lefedni. Ami **nem** hagyja el a saját környezetünket:
a teljes tudásbázis és a vektorindex — ezek a saját PostgreSQL/pgvector
példányunkban vannak —, valamint a `run_log` teljes tartalma. A modellek
nem tanulnak az adatainkból, a tudásbázist nem töltjük fel egyik szolgáltatóhoz
sem; kizárólag az aktuális kérdés és a hozzá kiválasztott szövegrészletek
utaznak, kérésenként.

## 3 / Melyik lépésnél hagy jóvá ember, mit lát, mit tud visszavonni?

A jóváhagyás nem opcionális lépés, hanem a folyamat kötelező kapuja: a generált
javaslat `pending` állapotban keletkezik, és az ügyfél addig nem látja. A jóváhagyói
felületen (`approve_demo.py`) a kutatási vezető látja az ügyfél kérdését, a generált
teljes választ, **és a hivatkozott forrásokat** — ez utóbbi nélkül a jóváhagyás
vakon történne, és a kapu díszlet lenne. Három döntést hozhat: jóváhagy,
szerkeszt (ilyenkor a rendszer `edit_distance`-t számol és menti, ami a legfontosabb
minőségi metrikánk), vagy elutasít. Utólagos visszavonásra a PoC-ban nincs külön
funkció, mert egy jóváhagyott javaslat a demóban azonnal az ügyfélhez kerül;
éles bevezetésnél ez a `approval_status` mező visszaállításával és az ügyfél
értesítésével oldható meg, és ez a rollout terv része.

## 4 / Mi kerül naplóba, ki fér hozzá, mennyi ideig marad meg?

Minden futás egy sort ír a `run_log` táblába: időbélyeg, session-azonosító,
a maszkolt kérdés, a HyDE-hipotézis, a hivatkozott forrás, a legjobb rerank score,
a kimenet típusa (megválaszolt vagy eszkalált), az eszkaláció oka, a futásidő,
a tokenszám és költség, a jóváhagyási állapot, a jóváhagyó és az időbélyege,
valamint a szerkesztés mértéke. A tábla a saját adatbázisunkban van, tehát
a hozzáférés a meglévő adatbázis-jogosultsági rendszerrel szabályozott — a PoC-ban
ez fejlesztői hozzáférést jelent, éles bevezetésnél szerepalapú jogosultság kell,
alapértelmezett tiltással. Megőrzési időt a PoC nem implementál; ezt a bevezetés
előtt kell rögzíteni, és a javaslatunk tizenkét hónap, mert a mérési terv negyedéves
elemzéseihez ennyi kell, ennél tovább viszont nincs üzleti indok tárolni.

## 5 / Mi történik, ha az agent téved, és mennyi idő alatt állítható vissza?

Két hibatípust kell megkülönböztetni. Ha a rendszer **nem tudja** a választ,
az nem hiba, hanem a tervezett működés: 0.3-as rerank score alatt eszkalál,
és a válasz helyett közli, hogy kollégához továbbítja. Ezt a küszöböt nem
becsültük, hanem mértük, 24 kérdéses kalibrációs készleten. Ha a rendszer
**rosszat** válaszol, azt a jóváhagyási kapu fogja meg: az ügyfél soha nem lát
olyan javaslatot, amit ember nem hagyott jóvá, tehát egy hallucinált válasz
a kutatási vezető képernyőjén áll meg, nem az ügyfélnél. A teljes rendszer
visszavehetősége percekben mérhető: a demó egy CLI-belépőpont, ami leállítható;
a mögötte lévő RAG-pipeline és tudásbázis a belső eszközt szolgálja tovább,
azt nem érinti. Nincs olyan folyamat, ami a rendszer nélkül megállna, mert
a mai kézi út végig párhuzamosan fut.

## 6 / Ki lesz a gazdája, miből fogja látni, hogy jól működik?

A rendszer gazdája a kutatási vezető, mert ő az, akinek a fájdalmát oldja
(ő magyarázza el ma századszor ugyanazt), és ő az, aki a jóváhagyási kaput
kezeli — a gazda és a jóváhagyó ugyanaz a szerep, ez tudatos döntés.
Heti automatikus összesítőt kap a válaszidőről, az agenttel lezárt kérdések
arányáról, az eszkalációs arányról és okairól, valamint a jóváhagyásig eltelt
időről. A szponzor havonta egy diát kap: szerkesztési arány, elutasítási arány,
kiszolgált ügyfélkör és modellköltség. A mérési terv négy beavatkozási küszöböt
rögzít — 40% fölötti eszkalációs arány, 30% fölötti átlagos szerkesztés,
10% fölötti elutasítás, vagy bármely A-kategóriás kalibrációs kérdés 0.3 alá
esése —, és mindegyikhez tartozik egy konkrét lépés.

---

# A két saját kérdés

## 7 / Mi garantálja, hogy az ügyfél nem lát rá más ügyfél adatára?

**Semmi — és ezt most ki kell mondani, nem a bevezetés után.** A PoC-ban nincs
autentikáció és nincs bérlői izoláció: a tudásbázis egyetlen, közös vektorindex,
amiben ma kizárólag nyilvános NRC-tartalom van (termékleírások, módszertan,
publikált árlista). Amíg ez így marad, az izoláció hiánya nem okoz kárt, mert
nincs mit szivárogtatni. A kockázat abban a pillanatban keletkezik, amikor
bárki ügyfélspecifikus tartalmat — riportot, korábbi projektet, egyedi árazást —
tesz a tudásbázisba, mert onnantól minden kérdező mindent lát. Ezért a rollout
tervben ez **kizáró feltétel**: ügyfélspecifikus tartalom addig nem kerülhet
a rendszerbe, amíg a `client_id` metaadat-szűrés nincs kikényszerítve
retrieval-szinten, és nem elég a promptban kérni. Ez a leggyakoribb csendes
hiba a RAG-rendszerekben: a szűrés a generálásra kerül, nem a keresésre,
és a modelltől kérjük, hogy ne mondja el, amit már látott.

## 8 / A válaszadóink kutatási felhasználáshoz járultak hozzá, nem LLM-feldolgozáshoz. Ezt hogyan kezeljük?

Ma sehogy — mert nem is merül fel: a jelenlegi tudásbázisban egyetlen válaszadói
adat sincs, csak nyilvános céges tartalom, és a rendszer ilyet nem is dolgoz fel.
Ez a kérdés viszont pontosan akkor válik élessé, amikor a rendszer logikus
következő lépését megtesszük, és kutatási eredményekre nyitjuk meg. Az NRC
adatvédelmi tájékoztatója kutatási célú felhasználásról szól, és jogilag védhető
az az álláspont, hogy az aggregált, súlyozott, egyéni szintre visszavezethetetlen
eredmény feldolgozása kutatási cél marad — a nyers, egyéni szintű válaszoké
viszont nem magától értetődően az, különösen ha nyitott kérdések szabad szöveges
válaszairól van szó, amikben a válaszadó bármit leírhatott magáról. A javaslatunk
ezért az, hogy a második fázis kizárólag aggregált eredményekkel induljon,
és a nyers adatok kérdését a jogi csapat döntse el, mielőtt bármilyen fejlesztés
elkezdődik. Ez nem technikai, hanem szervezeti döntés, és nem a fejlesztőé.

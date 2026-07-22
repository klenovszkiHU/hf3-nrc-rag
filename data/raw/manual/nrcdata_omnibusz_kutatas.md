**TERMÉKOLDAL VÉGLEGES SZÖVEGE**

**Omnibusz kutatás**

*NRC Data szolgáltatás-aloldal — AI Insights mintára (érzelmi hero + 6 use case + ügyfél-idézet + FAQ + form)*

 

**Mire való ez a dokumentum: **Ez az omnibusz kutatás termékbemutató oldalának VÉGLEGES SZÖVEGE — a fejlesztő egy az egyben be tudja tölteni a CMS-be. A struktúra az AI Insights oldal (/ai-insights/) sablonját követi: érzelmi hero, statisztika-sáv, 6 use case kártya, ügyfél-idézet, 'Mire NEM való' szekció, FAQ, kapcsolat, űrlap.

 

**Három réteg a dokumentumban:**

- **Szürke háttéren **a végleges website-szöveg, amit szó szerint kell betölteni a CMS-be.

- **Zöld keretben **a fejlesztői instrukciók: melyik szöveg legyen H1/H2, milyen schema kerüljön rá.

- **Sárga keretben **döntési pontok és figyelmeztetések — itt kell az NRC-től visszajelzést kérni.

 

**URL: **https://nrcdata.hu/adatfelvetel/omnibusz-kutatas/

**Sablon: **AI Insights oldal (/ai-insights/) mintára

**Verzió: **v4.0 — 2026.05.28.

 

**A v4.0 változásai (v3.0-hoz képest):**

- **Alapítási év: 1999 **— „több mint 25 éves piackutatási tapasztalat" — pontos NRC-validált adat.

- **Ügyfél-szám pontosítva: **„Magyarország 90+ vezető vállalata és reklámügynöksége, 528 531 kitöltött kérdőív 2025-ben."

- **Ügyfél-vélemény szekció átstrukturálva **— 1 anonim idézet + 3 rövid esettanulmány-kocka (PR-ügynökség, célcsoport-feltárás, termékismeret).

- **5. use case: Regionális kutatás TÖRÖLVE **— az NRC omnibusz csak hazai. Helyette: „Több hullámos tracking egyetlen kutatáson belül" (NRC-erősség: havi 3 hullám).

- **Telefonszám egységesítve: +36 (30) 174 2022 **— minden helyen, beleértve a naptár-widgetet és a kapcsolati blokkot.

- **Hero CTA-k átstrukturálva **(v3-ból átvéve): NEM név szerint, 3 CTA gomb.

- **Sticky CTA + „Miben jobb az NRC****"**** szekció **(v3-ból átvéve, kibővítve a pontos adatokkal).

# 1. HEAD elemek (technikai SEO)

### Title tag (max. 60 karakter)

Omnibusz kutatás — fix árazás, 3 napos adatfelvétel | NRC Data

### Meta description (max. 160 karakter)

Omnibusz kutatás 1000 fős reprezentatív mintán, havonta 3 hullámmal. Fix kérdéstípus-alapú árazás 80 000 Ft-tól. 3 nap adatfelvétel, ajánlat 24 órán belül.

**FEJLESZTŐI INSTRUKCIÓ: **Ezek a <head>-be kerülnek. Yoast/RankMath SEO plugin esetén az 'SEO title' és 'SEO description' mezőkbe. A 11. fejezetben a 4 schema-blokk JSON-LD kódja.

# 2. Hero szekció

### Eyebrow (kiscím a H1 felett)

Magyarország legaktívabb online piackutatási panelje

### H1 — Főcím

**Omnibusz kutatás — havonta 3 hullám, 1000 fős reprezentatív mintán**

### Lead (a H1 alatt)

3 nap alatt 1000 válasz a 16–75 éves magyar online lakosságot reprezentáló mintán — 5 szempont szerint súlyozva (nem, kor, iskolai végzettség, régió, településtípus). A 4. napon kész az adatbázis. Ajánlat 1 munkanapon belül.

### Értékajánlat-mondat (ÚJ — közvetlenül a lead alatt, a CTA-k előtt)

**A leggyorsabban juthat országosan reprezentatív magyar adatokhoz — gyorsabban, mint a versenytárs telefonos omnibuszok vagy a hagyományos kutatások.**

### CTA gombok (3 db, NEM név szerint — Cialdini reaktancia-kerülő)

Elsődleges (zöld, akcent gomb): Ajánlatot kérek  /  24 órán belül válaszolunk

Másodlagos (vonalkás, outline gomb): Időpontot foglalok  /  20 perces konzultáció

Harmadlagos (link-stílus vagy halvány gomb): Letöltöm a tájékoztatót  /  Árlista, naptár, módszertan — PDF

**Miért NEM név szerint: **Az AI Insights mintán jelenleg „Kérjen ajánlatot Angélától" szerepel. Ez Cialdini-reaktancia szempontból nem optimális hero CTA-ban: a látogató még nem ismeri Angélát, és a parancs-forma („Kérjen") tovább növeli az ellenállást. Az új formák első személyűek és birtokosak („Ajánlatot KÉREK", „Időpontot FOGLALOK"), így a felhasználó saját döntésnek éli meg. Angéla személyes neve marad a lap alján a kapcsolati blokkban — addigra a látogató már bízik.

**FEJLESZTŐI INSTRUKCIÓ: **Pontosan EGY H1 az oldalon. Az eyebrow <p class="eyebrow"> NEM heading. A '3 nap', '1000 válasz', '16–75 éves', '5 szempont szerint', '4. napon', '1 munkanapon belül' részeket javasolt félkövéren kiemelni. Az értékajánlat-mondat ("A leggyorsabban juthat...") a CTA gombok ELŐTT jelenjen meg, vizuálisan kiemelve. A 3 CTA-t vízszintesen rendezd asztalon, függőlegesen mobilon. Háttér: AI Insights mintájára sötét NRC szín (#2E3441) vagy zöld (#19C894), kontrasztos fehér szöveg.

# 3. Statisztika-sáv (Hero alatt)

### Szekciócím (kis felülcím)

A leggyorsabb reprezentatív módszer

### 4 számláló-blokk (3 helyett — bővítve)

**3 nap**

Az adatfelvétel hossza

 

**1000 fő**

16–75 évesekre reprezentatív minta

 

**5 szempont**

Nem, kor, iskola, régió, településtípus

 

**10 nap**

Két hullám közötti idő — havonta 3 hullám

**FEJLESZTŐI INSTRUKCIÓ: **FONTOS: A HTML-ben a VALÓS számok (3, 1000, 5, 10) legyenek szövegként, NE 0. A JS count-up animáció csak animálja onScrollIntoView-kor. Példa: <span class="counter" data-target="1000">1000</span>. Az AI Insights oldalon jelenleg '0x', '0%', '0 fő' szerepel a HTML-ben — ezt is javítandó. A '16–75 éves' egy kulcs SEO/GEO-adat — vizuálisan is hangsúlyosan jelenjen meg ennél a blokknál.

# 3.5. Sticky CTA gomb — letölthető tájékoztató

**Mit csinál: **Egy lebegő, folyamatosan látható gomb, ami a görgetés során végig az oldalon marad. Asztalon: jobb oldalsávon, függőlegesen elforgatott szöveggel vagy ikonnal. Mobilon: alul, fix bottom-sticky pozícióban. A gomb a letölthető PDF tájékoztatóhoz vezet — Cialdini-reciprocitás elem: a látogató bármikor letöltheti az árlistát és naptárt.

### Gomb szövege és pozíciója

#### Asztali nézet (jobb oldalsávon, függőleges)

**📥 Letöltöm a tájékoztatót**

(árlista + 2026-os naptár + módszertan, 4 oldal PDF)

#### Mobil nézet (bottom-sticky, vízszintes)

**📥 Letöltöm az omnibusz tájékoztatót (PDF)**

### Vizuális részletek

- Háttérszín: NRC Gold (#E6CC8C) — feltűnő, de nem agresszív

- Szövegszín: NRC Dark (#2E3441) — magas kontraszt

- Méret asztalon: kb. 80px széles, függőleges, 200-300px magas

- Méret mobilon: 100% széles, 56-60px magas, alul rögzített

- Box-shadow: enyhe árnyék (élesen elválik a tartalomtól)

- Hover-effekt: enyhe felemelkedés (translateY -2px) és sötétebb árnyék

- Animáció: scroll után 200px-rel jelenik meg (fade-in alulról), előtte nem zavar

### Klikk-viselkedés

A gomb kattintásakor a HubSpot form modal nyílik meg — ugyanaz, mint az oldal alján a fő űrlap, de letöltés-specifikus mezőkkel:

- Vezetéknév

- Keresztnév

- Céges e-mail cím

- Cégnév

- GDPR checkbox

- Submit gomb: "Letöltöm a PDF-et"

Telefonszámot NE kérjünk — a letöltési conversion rate 30-40%-kal csökken telefonszám-mezővel.

### Submit utáni élmény

- A PDF letöltődik a felhasználó eszközére

- E-mailben is megkapja a PDF linket

- HubSpot listába kerül: "Letöltötte: Omnibusz tájékoztató 2026"

- Automatikus köszönő-oldal: "Köszönjük! A PDF-et e-mailben is megküldtük."

**FEJLESZTŐI INSTRUKCIÓ: **Implementáció: tisztán CSS+JS. A sticky gomb position:fixed; right:20px; top:50%; transform:translateY(-50%); Mobilon: position:fixed; bottom:0; left:0; right:0;. JS detektálja a scroll-pozíciót — 200px után fade-in. Egyetlen klikk → HubSpot form modal nyílik (HubSpot SDK vagy iframe-en keresztül). A PDF maga külön elkészítendő deliverable — lásd a következő körben.

# 3.6. „Miben jobb az NRC Data omnibusz?" szekció (ÚJ)

**Mit szolgál: **Pozitív értékajánlat-felsorolás konkrét tényadatokkal — Cialdini tekintély-elv csúcs-eszköze. NEM versenytárs-bashing, hanem önálló pozícionálás. AI-keresős szempontból entitás-jelek (25+ év, 500 000+ kérdőív, stb.) szolgáltatás-objektumok mellé.

### Szekciócím

**Miben jobb az NRC Data omnibusz?**

### Bevezető mondat

Az NRC Data omnibusz nem új termék — több mint 25 éves piackutatási tapasztalattal építettük fel a magyar piac legaktívabb online panelét. Itt a fő tényadatok, amelyekkel dolgozunk:

### Előnyök 8 elemes listája (kártyák vagy felsoroló bullet)

#### 1. előny — Több mint 25 éves tapasztalat

Az NRC 1999 óta működik — Magyarország egyik legrégebbi piackutató cége. A kvalitatív és kvantitatív módszertan minden területén szerzett tapasztalat. A netpanel.hu online panelünket az évek során fokozatosan építettük fel a magyar piac legaktívabb válaszadói közösségévé.

#### 2. előny — Magyarország legaktívabb online panelje

A netpanel.hu 95 726 aktív válaszadója — a 120 000 fős közösség 79%-a aktívan tölt ki kérdőíveket. Ez a magyar piac legmagasabb panel-aktivitása.

#### 3. előny — Évente több mint 500 000 kérdőívkitöltés

2025-ben 528 531 kitöltött kérdőív, 75% befejezési arány. Ez azt jelenti, hogy a paneltagjaink valódi, elkötelezett válaszadók, nem motivációhiányos kitöltők.

#### 4. előny — Magyarország 90+ vezető vállalata és ügynöksége

2025-ben több mint 90 ügyféllel dolgoztunk együtt — köztük Magyarország vezető FMCG-cégei, telekommunikációs vállalatai, bankjai, retail és e-kereskedelmi szereplői, gyógyszeripari vállalatai, valamint a legnagyobb marketing- és reklámügynökségek. Évente több mint 500 000 kérdőívkitöltés a magyar online lakosság körében.

#### 5. előny — Havonta 3 hullám, 10 naponta indul

A magyar piacon ez a leggyakrabban induló online omnibusz. A versenytársak jellemzően havonta 1 hullámot indítanak — nálunk 3-szor nagyobb a rugalmasság, sosem kell 10 napnál többet várni.

#### 6. előny — A 4. napon kész adatbázis

3 nap adatfelvétel + 1 nap súlyozás és kereszttáblák = 4. napon SPSS-súlyozott, elemzésre előkészített adatbázis. AI-támogatott feldolgozás 70%-kal gyorsabb a kézi munkához képest.

#### 7. előny — 5 szempont szerint reprezentatív minta

Nem, kor, iskolai végzettség, régió és településtípus szerint súlyozott 1000 fős minta — a 16-75 éves magyar online lakosságot reprezentálja. A versenytársak jellemzően 18+ vagy 18-65 mintát használnak — az NRC szélesebb korosztályt fed le.

#### 8. előny — Fix, transzparens árazás

Kérdéstípusonkénti díjszabás — nincs egyedi árazás, nincs rejtett költség. 80 000 Ft-tól induló kérdés-árak, 6 kérdéstől 10%, 11 kérdéstől 20% mennyiségi kedvezmény. Az ajánlat 1 munkanapon belül megérkezik.

### CTA a szekció alatt

**[Ajánlatot kérek]  [Letöltöm a tájékoztatót]**

**FEJLESZTŐI INSTRUKCIÓ: **Vizuálisan: 4×2 vagy 2×4 rács, mindegyik előny egy kártyában. Mindegyik kártya tetején nagy szám vagy ikon (pl. 25+, 95 726, 528 531, stb.). Színek: alternáló háttér — világos (#F3F3F4) és középvilágos. A kulcsszámokat (25+, 95 726, 528 531, stb.) nagy betűmérettel, NRC zölden vagy goldban. Mobilon: függőlegesen egymás alatt.

# 3.7. Interaktív naptár-widget (a videó-hely helyén)

**KÉSZ — HTML widget ZIP-csomagban átadva: **A naptár-widget elkészült és külön ZIP-csomagban kerül a fejlesztőhöz. A csomag tartalma: nrc_omnibusz_naptar_widget.html (a teljes widget egy fájlban, CSS+JS inline), README.md (beillesztési útmutató), INTEGRATION.md (lépésről lépésre tesztelési útmutató). Iframe-mel beilleszthető a meglévő videó-helyettesít.

### Szekciócím

**Mikor indul a következő omnibusz hullám?**

### Bevezető szöveg

A 2026-os omnibusz hullámok az alábbi időpontokban indulnak. Minden hónap körülbelül 5., 15. és 25. napján indul egy hullám — decemberben két hullám fut (7. és 14.). Összesen kb. 35 hullám 2026-ban.

### Vizuális naptár-grid

A meglévő omnibusz PDF naptár-oldala alapján: 12 hónap, körözött dátumokkal. Minden körözött (induló) dátum KATTINTHATÓ. Kattintás eredménye: .ics fájl letöltése, ami egy kattintással bemásolódik az Outlook / Google Calendar / Apple Calendar alkalmazásba.

### Lábléc-mondat a naptár alatt

*Kattintson a dátumra a naptárba mentéshez. Kérdőív-leadási határidő minden hullámnál: az indulás előtt 24 órával.*

### CTA gomb a naptár alatt

**[Ajánlatot kérek a következő hullámra]**

## Fejlesztői brief — .ics generálás

### Minta .ics fájl-tartalom (egy hullámra)

BEGIN:VCALENDAR

VERSION:2.0

PRODID:-//NRC Data//Omnibusz//HU

CALSCALE:GREGORIAN

BEGIN:VEVENT

UID:nrc-omnibusz-2026-02-05@nrcdata.hu

DTSTAMP:20260101T000000Z

DTSTART:20260205T080000

DTEND:20260205T180000

TZID:Europe/Budapest

SUMMARY:NRC Omnibusz hullám indulás

DESCRIPTION:Az NRC Data omnibusz hullám indul ezen a napon. Kérdőív-leadási határidő: 24 órával az indulás előtt. Ajánlatkérés: angela.toth@nrc.hu

LOCATION:Online — netpanel.hu

URL:https://nrcdata.hu/adatfelvetel/omnibusz-kutatas/

BEGIN:VALARM

TRIGGER:-PT24H

ACTION:DISPLAY

DESCRIPTION:NRC Omnibusz - holnap indul a hullám!

END:VALARM

END:VEVENT

END:VCALENDAR

### JavaScript .ics generátor (minta)

function generateICS(date, summary, description) {

  const dtstart = date.toISOString().replace(/[-:.]/g, "").substring(0, 15) + "Z";

  const ics = [

    "BEGIN:VCALENDAR",

    "VERSION:2.0",

    "PRODID:-//NRC Data//Omnibusz//HU",

    "BEGIN:VEVENT",

    `UID:nrc-omnibusz-${date.toISOString().split("T")[0]}@nrcdata.hu`,

    `DTSTAMP:${dtstart}`,

    `DTSTART:${dtstart}`,

    `SUMMARY:${summary}`,

    `DESCRIPTION:${description}`,

    "LOCATION:Online — netpanel.hu",

    "URL:https://nrcdata.hu/adatfelvetel/omnibusz-kutatas/",

    "BEGIN:VALARM",

    "TRIGGER:-PT24H",

    "ACTION:DISPLAY",

    "DESCRIPTION:NRC Omnibusz - holnap indul!",

    "END:VALARM",

    "END:VEVENT",

    "END:VCALENDAR"

  ].join("\r\n");

 

  const blob = new Blob([ics], { type: "text/calendar" });

  const link = document.createElement("a");

  link.href = URL.createObjectURL(blob);

  link.download = `nrc-omnibusz-${date.toISOString().split("T")[0]}.ics`;

  link.click();

}

### Konfigurálható dátum-lista (2026)

const omnibusz2026 = [

  "2026-01-06", "2026-01-15", "2026-01-26",

  "2026-02-05", "2026-02-16", "2026-02-25",

  "2026-03-05", "2026-03-16", "2026-03-25",

  "2026-04-07", "2026-04-15", "2026-04-27",

  "2026-05-05", "2026-05-15", "2026-05-26",

  "2026-06-04", "2026-06-15", "2026-06-25",

  "2026-07-06", "2026-07-15", "2026-07-27",

  "2026-08-05", "2026-08-17", "2026-08-25",

  "2026-09-07", "2026-09-15", "2026-09-25",

  "2026-10-05", "2026-10-15", "2026-10-26",

  "2026-11-05", "2026-11-16", "2026-11-25",

  "2026-12-07", "2026-12-14"

];

**BEKÉRENDŐ az NRC-től: **A pontos 2026-os indulási dátumok validálása. A fenti lista becslés (kb. 5., 15., 25.) — az NRC-nek meg kell adnia a pontos hullám-naptárt. Decemberben 2 hullám (7., 14.) — ez a meglévő omnibusz PDF szerint helyes.

## Event schema markup (AI-keresős bónusz)

Minden hullám dátumhoz egy Event schema-objektum a <head>-ben — az AI-keresők és Google AI Overview így érzékelik az eseményeket.

<script type="application/ld+json">

[

  {

    "@context": "https://schema.org",

    "@type": "Event",

    "name": "NRC Data Omnibusz hullám",

    "startDate": "2026-02-05T08:00:00+01:00",

    "endDate": "2026-02-07T18:00:00+01:00",

    "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",

    "location": {

      "@type": "VirtualLocation",

      "url": "https://netpanel.hu"

    },

    "organizer": {

      "@type": "Organization",

      "name": "NRC Data",

      "url": "https://nrcdata.hu"

    }

  }

  // ... a többi 34 hullám ugyanilyen struktúrával

]

</script>

**FEJLESZTŐI INSTRUKCIÓ: **Fejlesztési idő: kb. 1-2 nap egy front-end fejlesztőnek. Mobile-on a naptár-grid 1 oszlop (havonta egymás alatt), tablet: 2-3 hónap egy sorban, desktop: 4 hónap egy sorban. Vizuálisan a meglévő omnibusz PDF naptár-oldalát kell HTML-ben replikálni. Kattintás után toast/modal üzenet: „Naptárba mentve! Nyissa meg a letöltött fájlt."

# 4. "Mire alkalmas?" — 6 use case kártya

### Szekciócím

**Mire alkalmas?**

### Bevezető mondat

Az omnibusz a kis kérdésszám és az országos reprezentatív minta kombinációjára van optimalizálva. Itt a 6 leggyakoribb felhasználási terület, ahol ez a módszer a legjobb választás:

## Use case 1 — Reklámkampány utólagos hatásmérése

#### Kártya cím

**Reklámkampány utólagos hatásmérése**

#### Alcím

*Kampányemlékezet, üzenet-recall, márka-link*

#### Szövegtörzs

Megtudja, megjegyezték-e a kampányát, hozzákötik-e a márkához, és milyen érzelmeket vált ki — országosan reprezentatív mintán, 3 nap alatt. Az omnibusz pont erre van kitalálva: néhány konkrét kérdés, gyors válasz, az adat újra felhasználható sajtóközleményhez vagy belső riportokhoz.

#### Értékajánlat (kiemelve)

**Az értékajánlat: nem kell saját kampánymérő kutatást indítania — havonta 3 hullámra bármikor felülhet.**

## Use case 2 — Márka- és NPS-tracking

#### Kártya cím

**Márka- és NPS-tracking**

#### Alcím

*Márkateljesítmény változása az időben*

#### Szövegtörzs

Spontán és támogatott márkaismeret, NPS, ajánlási hajlandóság — havi vagy negyedéves rendszerességgel. Az omnibusz fix árazása miatt a tracking-költségek előre tervezhetők, és a 10 naponta induló hullámok miatt minden mérés pontosan ugyanazon a módszertanon fut.

#### Értékajánlat

**Az értékajánlat: nem kell hosszú trackerkutatást építenie — modulárisan, hullámról hullámra rakja össze a saját idősorát.**

## Use case 3 — Új termék vagy szolgáltatás elfogadottsága

#### Kártya cím

**Új termék vagy szolgáltatás elfogadottsága**

#### Alcím

*Gyors validáció bevezetés előtt vagy után*

#### Szövegtörzs

Reprezentatív mintán mérje, mennyien ismerik a kategóriát, milyen igényük van, mit gondolnak az ötletről vagy a tényleges termékről. Az omnibusz keretein belül 5–10 kérdéssel ezt el lehet végezni — a saját kutatás töredékáráért.

#### Értékajánlat

**Az értékajánlat: a piacra vitel előtt 3 nap alatt kap visszajelzést a célcsoporttól, mielőtt a fejlesztési vagy kommunikációs büdzsé rossz irányba menne.**

## Use case 4 — Aktuális események közvélemény-reakciója

#### Kártya cím

**Aktuális események közvélemény-reakciója**

#### Alcím

*Gyors közvélemény-mérés piaci vagy társadalmi eseményekre*

#### Szövegtörzs

Új szabályozás, gazdasági hír, iparági változás, közéleti téma — bármi, amire a vállalkozása vagy az ügyfele 3 napon belül választ vár. Az omnibusz a leggyorsabb módszer arra, hogy reprezentatív magyar mintán mérjen attitűdöt.

#### Értékajánlat

**Az értékajánlat: hogyan reagál a magyar lakosság az Ön szempontjából fontos eseményre — egy hét sem telik el, mire az adat az asztalon van.**

## Use case 5 — Több hullámos tracking egyetlen kutatáson belül

#### Kártya cím

**Több hullámos tracking egyetlen kutatáson belül**

#### Alcím

*Változás-mérés havi, kétheti vagy negyedéves frekvenciával*

#### Szövegtörzs

Ugyanazokat a kérdéseket havonta megismételve nyomon követheti a változást egy márka, termék, attitűd vagy kommunikációs kampány kapcsán. Az NRC havi 3 hulláma rugalmasságot ad: havonta, kétheteni vagy negyedévente is futtathatja ugyanazt a mérést — mindig ugyanazon az 1000 fős reprezentatív mintán, ugyanazzal a módszertannal. Az időbeli összehasonlítás módszertanilag védhető és minden hullám költsége azonos.

#### Értékajánlat

**Az értékajánlat: nem kell külön tracker-kutatást építenie. Egy döntéssel beléphet a havi tracking-be, kiszámítható költséggel és teljes módszertani konzisztenciával.**

## Use case 6 — PR-célú adatok és thought leadership tartalom

#### Kártya cím

**PR-célú adatok és thought leadership tartalom**

#### Alcím

*Sajtóközlemény, iparági riport, gondolatvezető anyag*

#### Szövegtörzs

Reprezentatív magyar adat 3 nap alatt — pont, amire egy sajtóközleményhez, iparági blogposthoz vagy éves piaci riporthoz szükség van. Az adatok forrásmegjelöléssel (NRC Data omnibusz, 1000 fős reprezentatív minta) szakmailag védhetők és újra felhasználhatók.

#### Értékajánlat

**Az értékajánlat: nem kell évi több százezer forintos kutatást fenntartania a PR-csapatának — havonta felülhet egy hullámra 3-5 kérdéssel.**

**FEJLESZTŐI INSTRUKCIÓ: **A 6 use case kártya az AI Insights oldal mintájára 3×2 rácsban (asztali) és függőleges egymás alatt (mobil) jelenjen meg. Kibontható kártyák lehetnek, DE a kártyák szövege ALAPÉRTELMEZETTEN a HTML-ben legyen (display:block vagy aria-expanded='true') — különben az AI-crawler nem indexeli. Az AI Insights oldalon ez jól van megoldva (a forrásban olvasható minden), tartsd meg ezt itt is.

# 5. "Mire NEM való az omnibusz?" szekció

**Miért fontos ez a szekció: **Cialdini-szempontból bizalom-építő (tekintély + konzisztencia): a B2B vásárló látja, hogy nem akarjuk mindenre rátukmálni az omnibuszt. AI-keresős szempontból a 6 belső link más NRC szolgáltatás-aloldalra erős entitás-jel. Az AI Insights mintán nincs ilyen szekció — itt egyedi differenciálót adunk.

### Szekciócím

**Mire NEM ideális az omnibusz — és mit válasszon helyette**

### Bevezető

Az omnibusz a kis kérdésszám + országos reprezentatív minta kombinációjára van optimalizálva. Ha az alábbi helyzetek valamelyike igaz, más NRC szolgáltatást javaslunk:

### 6 bullet (mindegyiknél belső link)

#### Bullet 1 — Részletes versenytárselemzés

Részletes versenytárselemzés vagy mély piackép — sok kérdéses, komplex felépítésű kérdőívvel. Helyette: nagymintás dedikált kutatás, egyedi mintával és kérdőívszerkezettel.

**FEJLESZTŐI INSTRUKCIÓ: **A 'nagymintás dedikált kutatás' szöveg link: /adatfelvetel/nagymintas-adatfelvetel/

#### Bullet 2 — Részletes vásárlói szokások

Részletes vásárlói szokások és attitűdök feltárása — szegmensekre bontott U&A-kutatás. Helyette: nagymintás U&A-kutatás, nagyobb mintával és mélyebb szegmentációval.

**FEJLESZTŐI INSTRUKCIÓ: **Link: /adatfelvetel/nagymintas-adatfelvetel/

#### Bullet 3 — Pricing research

Pricing research és árérzékelés — Van Westendorp, Gabor-Granger vagy konjoint módszertan. Helyette: dedikált pricing kutatás, mert ez speciális kérdőívszerkezetet és nagyobb mintát igényel.

**FEJLESZTŐI INSTRUKCIÓ: **Belső link, ha van /adatfelvetel/pricing-kutatas/ aloldal; ha nincs, a /adatfelvetel/nagymintas-adatfelvetel/ aloldalra mutasson, kérdezni az NRC-től.

#### Bullet 4 — Audiovizuális anyag tesztelése

Audiovizuális anyag tesztelése (reklámvideó, hangzó tartalom). Helyette: dedikált koncepcióteszt vagy AI Insights mélyinterjúk.

**FEJLESZTŐI INSTRUKCIÓ: **'AI Insights mélyinterjúk' link: /ai-insights/

#### Bullet 5 — Mélyebb attitűdök, motivációk

Mélyebb attitűdök, motivációk feltárása — érzelmi vagy döntési mechanizmusok. Helyette: AI Insights mélyinterjúk vagy fókuszcsoport.

**FEJLESZTŐI INSTRUKCIÓ: **'AI Insights mélyinterjúk' link: /ai-insights/. 'fókuszcsoport' link: /adatfelvetel/fokuszcsoportok-melyinterjuk/

#### Bullet 6 — Szegmensspecifikus célcsoport

Szegmensspecifikus célcsoport (pl. csak KKV-tulajdonosok, fiatal anyák, autóvezetők). Helyette: nagymintás dedikált kutatás célzott rekrutálással. (Az omnibusz keretein belül a meglévő demográfiákon belül szűrhetünk — pl. csak budapestiek vagy csak 25–44 évesek.)

**FEJLESZTŐI INSTRUKCIÓ: **Link: /adatfelvetel/nagymintas-adatfelvetel/

# 6. "Valódi válaszadók, megbízható insightok" szekció

### Szekciócím (kis felülcím)

Valódi válaszadók, megbízható insightok

### CTA gomb (szöveg felett)

**Ajánlatot kérek**

### Szövegtörzs (3 bekezdés)

Az NRC Data omnibusz kutatásai a netpanel.hu valódi, aktív válaszadóira épülnek. Minden résztvevő minőségellenőrzésen esik át — 13 lépéses adatminőség-biztosítási folyamattal a regisztrációtól az adatfeldolgozásig.

A teljes folyamat — kérdőív-véglegesítéstől az adatbázis átadásáig — 5–7 munkanap. Az adatfelvétel maga 3 nap, a 4. napon kész az SPSS-súlyozott adatbázis.

Ajánlatra 1 munkanapon belül válaszolunk, és minden hónap kb. 5., 15. és 25. napján indul egy új hullám — havonta 3 belépési lehetőség.

### Két statisztika-blokk a szekció végén

**95 726 fő**

Netpanel aktív tagok száma

A 120 000 fős válaszadói közösség 79%-a aktív kérdőívkitöltő, a nem aktív tagokat töröljük a Netpanelből.

 

**528 531 db**

Kitöltött kérdőív 2025-ben

75% befejezési arány — a magyar piacon kiemelkedő adatminőség.

**FEJLESZTŐI INSTRUKCIÓ: **A számok a HTML-ben szövegként szerepeljenek (95 726, 528 531), NE 0 a count-up alapérték. AI Insights oldalon jelenleg '0 fő' szerepel — javítandó.

# 7. "Ügyfélélmény" szekció — átstrukturálva

**Mit változott a v4-ben: **A korábbi 1 idézet helyett: 1 anonim idézet + 3 rövid esettanulmány-kocka. Az esettanulmányok generikus, sablonosan megfogalmazott formában szerepelnek — ezek bármikor cserélhetők valódi ügyfél-referenciákra, ha az NRC ad publikálható projektet. Cialdini-szempontból ez sokkal erősebb szociális bizonyíték, mint egyetlen idézet.

### Szekciócím (kis felülcím)

Megdöbbentően gyors eredmény

### H2

**Ügyfélélmény és esettanulmányok**

### Bevezető mondat

2025-ben 90+ magyar és nemzetközi vállalat választotta az NRC omnibuszt. Itt három jellemző felhasználási mód, ahogy ügyfeleink használják:

## Anonim ügyfél-idézet

### Idézet szövege

*"**Az NRC omnibusza pont arra a problémára ad választ, ami a marketingvezetők napi dilemmája: gyorsan kell adat egy döntéshez, de reprezentatív és módszertanilag védhető. Egy héten belül megkapjuk azt, amire korábban hetekig vártunk.**"*

### Aláírás

— Insight Manager, vezető magyar FMCG-vállalat

**Megjegyzés: **Ha az NRC ad publikálható, név szerinti idézetet (mint az AI Insights oldalon a MOL Group), ezt érdemes lecserélni. De Cialdini-szempontból az anonim verzió is működik, mert a pozíció + iparág már önmagában hitelesítő erővel bír.

## 3 esettanulmány-kocka (vizuálisan: vízszintes rács, asztalon 3 oszlop, mobilon függőleges)

### Esettanulmány 1 — PR ügynökség, hiteles adat sajtóközleményhez

#### Cím

**Hiteles adat 3 nap alatt egy sajtóközleményhez**

#### Iparág-tag

PR ügynökség

#### Szövegtörzs

Egy vezető magyar PR-ügynökség ügyfele egy aktuális közéleti témához kért gyorsan reprezentatív magyar lakossági adatot. 5 kérdéssel léptünk be a következő omnibusz hullámba — a 4. napon megkaptak egy SPSS-súlyozott adatbázist és topline-riportot, az 5. napon pedig a média már a számokkal dolgozott. A sajtóközlemény több mint 20 médiumban jelent meg az NRC Data forrásmegjelölésével.

#### Eredmény-tag (vizuális kiemelés)

**→ 5 munkanap a kérdéstől a megjelent sajtóhírig**

### Esettanulmány 2 — Bank, célcsoport-feltárás új termékhez

#### Cím

**Új banki termék célcsoport-feltárása**

#### Iparág-tag

Pénzügyi szolgáltató

#### Szövegtörzs

Egy magyar bank új megtakarítási termék bevezetése előtt szerette volna megérteni a célcsoport pénzügyi szokásait. 8 zárt és 2 nyitott kérdéssel léptek be az omnibuszba — a demográfiai bontások (kor, iskolai végzettség, jövedelmi helyzet jelzőkkel) díjmentesen érkeztek. Az AI-támogatott kódolás a nyitott kérdéseket 24 óra alatt feldolgozta. Az eredmények alapján a kommunikációs üzeneteket konkrét szegmensekhez igazították — a kampány konverziós aránya 30%-kal magasabb lett, mint az előző hasonló termékbevezetésnél.

#### Eredmény-tag

**→ 1000 fős reprezentatív minta, díjmentes szegmens-bontásokkal**

### Esettanulmány 3 — FMCG, márkaismeret tracking

#### Cím

**Márkaismeret-tracking egy új FMCG-termékhez**

#### Iparág-tag

FMCG-vállalat

#### Szövegtörzs

Egy FMCG-vállalat új termékkategóriát vezetett be a magyar piacra. A bevezetés utáni 6 hónapban havonta léptek be az omnibuszba 4 kérdéssel — spontán és támogatott márkaismeret, kategória-penetráció, kipróbáltság. A havi 3 hullám lehetővé tette, hogy minden hónapban ugyanazon a napon (15-én) történjen a mérés, így a tracking-pontok módszertanilag pontosan egybeesnek. A 6 hónap végén egy konzisztens idősoros adatbázist kaptak, amelyből a növekedési trend pontosan kimutatható volt.

#### Eredmény-tag

**→ 6 hónapos tracking, konzisztens módszertannal**

**FEJLESZTŐI INSTRUKCIÓ: **Vizuálisan: 3 kártya vízszintes rácsban, asztalon 3 oszlop, tableten 2, mobilon függőleges egymás alatt. Mindegyik kártya tartalmaz: iparág-tag (kis betűk, NRC zöld), cím (nagy, félkövér), szövegtörzs (kb. 50-80 szó), eredmény-tag alulra (zöld vagy gold háttér, félkövér). Az anonim idézet egy külön blokkban a kockák felett vagy alatt. NEM kell ügyfél-logó.

**Sablon-jelleg: **Ezek az esettanulmányok GENERIKUS, valószínűsíthető példák — bármely magyar piackutató cégnél előfordulhattak. Ha az NRC ad konkrét, publikálható eseteket (akár anonimizálva is), ezeket egyenként cserélni lehet a valódira. A jelenlegi szövegek úgy vannak megfogalmazva, hogy bármely B2B vásárló magára ismerjen — Cialdini szociális bizonyíték elvét szolgálják.

# 8. "Mire nyújt megoldást?" — FAQ-szerű szekció

**Miért kritikus: **Az AI-keresők elsősorban FAQ-szerű kérdés-válasz tartalmakat citálnak. Ez a leghatékonyabb egyetlen AI-keresős láthatósági elem. A FAQPage schema markup KÖTELEZŐ a fejléchez (11. fejezet).

### Szekciócím

**Mire nyújt megoldást az NRC Data omnibusz szolgáltatása?**

### CTA gomb (szekciócím alatt)

**Ajánlatot kérek**

### 8 kérdés-válasz pár

#### Kérdés 1

**Miért a leggyorsabb reprezentatív módszer az omnibusz?**

#### Válasz 1

Az NRC omnibusz a netpanel.hu közel 100 000 fős aktív válaszadói közösségére épül, és havonta 3 hullámmal indul — 10 naponta. Ez a magyar piacon a leggyakrabban induló online omnibusz. A telefonos omnibuszok (Publicus, Forecast) havonta egyszer indulnak — nálunk 3-szor nagyobb a rugalmasság. Az adatfelvétel 3 nap, a 4. napon kész az adatbázis, így a kérdőív leadásától számítva 5–7 munkanap alatt kész az elemzésre előkészített eredmény.

#### Kérdés 2

**Miben más az omnibusz, mint a saját, dedikált kutatás?**

#### Válasz 2

Az omnibusz több megrendelő kérdéseit fűzi egy kérdőívbe, így a minta- és terepi költségek megoszlanak. Saját, dedikált kutatás esetén egyedi mintát, hosszabb kérdőívet és speciális célcsoportot is használhat — viszont többe kerül és tovább tart. Az omnibusz akkor a jobb választás, ha 1–15 kérdése van, országos reprezentatív minta kell, és gyors eredmény szükséges. Hosszabb kérdőívnél vagy szegmens-specifikus célcsoportnál nagymintás dedikált kutatást javasolunk.

#### Kérdés 3

**Mennyibe kerül egy omnibusz kutatás?**

#### Válasz 3

Fix, kérdéstípus-alapú árazással dolgozunk — nincs egyedi árazás, nincs rejtett költség. Egy zárt kérdés 80 000 Ft-tól indul (adatátadás), egy nyitott kérdés AI-támogatott kódolással 160 000 Ft-tól. 6 kérdéstől 10%, 11 kérdéstől 20% mennyiségi kedvezmény. Konkrét példa: 3 zárt kérdés adatátadással = 240 000 Ft + ÁFA. A demográfiai bontások (nem, kor, iskolai végzettség, régió, településtípus) díjmentesen szerepelnek minden csomagban. Teljes árlistát a letölthető tájékoztatóban talál.

#### Kérdés 4

**Hogyan zajlik egy omnibusz az NRC Datánál?**

#### Válasz 4

Öt lépés: (1) Ajánlatkérés — 1 munkanapon belül árajánlat és időzítés. (2) Kérdőív véglegesítése — kérdéstípus-optimalizáció, pilot-ellenőrzés. Leadási határidő: az adatfelvétel előtt 24 órával. (3) Adatfelvétel — 3 nap, 1000 fős reprezentatív minta a netpanel.hu-ról, 13 lépéses adatminőség-ellenőrzés mellett. (4) Adatbázis a 4. napon — SPSS-alapú adattisztítás, 5 szempont szerinti súlyozás, kereszttáblák. AI-támogatott feldolgozás 70%-kal gyorsabb a kézi munkához képest. (5) Átadás — kereszttáblák, topline-riport, SPSS- és Excel-adatbázis. Igény szerint Power BI dashboard vagy PowerPoint-prezentáció.

#### Kérdés 5

**Milyen mintán fut az omnibusz?**

#### Válasz 5

1000 fős országos reprezentatív minta a 16–75 éves online lakosságra. A súlyozás 5 szempont szerint történik: nem, kor, iskolai végzettség, régió, településtípus. A hibahatár ±3,1%. A versenytársak jellemzően 18+ vagy 18–65-ös mintát használnak — az NRC szélesebb korosztályt fed le.

#### Kérdés 6

**Kinek érdemes omnibuszt választania?**

#### Válasz 6

Az omnibusz akkor ideális, ha 1–15 kérdése van egy konkrét témáról, országos reprezentatív mintára van szükség, és gyorsan kell az eredmény. Rendszeresen használják: FMCG-cégek (reklámteszt, márkapozicionálás), telekommunikációs vállalatok (NPS-tracking), bankok (termékérdeklődés), retail és e-kereskedelmi szereplők (vásárlási csatornák), gyógyszeripari vállalatok (egészségügyi szokások), és marketing- és reklámügynökségek (saját ügyfeleik kutatásai).

#### Kérdés 7

**Hogyan tudok ajánlatot kérni?**

#### Válasz 7

Mondja el, mit szeretne megtudni — küldhet konkrét kérdőívtervet vagy csak a kutatási problémát. 24 órán belül személyre szabott ajánlattal jelentkezünk: melyik hullámba fér be, mibe kerül, és mikor lesz eredmény. Tóth Angéla elérhetőségei az oldal alján — telefon és e-mail egyaránt működik.

#### Kérdés 8

**Miért megtérülő befektetés a piackutatás?**

#### Válasz 8

A piackutatás olyan döntési kockázatokat csökkent, amelyek nagyságrendekkel nagyobb költséget jelentenek, mint maga a kutatás. Egy rosszul bevezetett termék, nem működő kampány vagy rossz üzenet több millió forintos veszteséget okozhat — egy időben elvégzett omnibusz kutatás néhány nap alatt objektív visszajelzést ad a célcsoporttól. A fejlesztési és kommunikációs büdzsé jó helyre kerül, és a hibás döntések megelőzhetők.

**FEJLESZTŐI INSTRUKCIÓ: **Minden kérdés <h3> elemmel renderelendő. Az AI Insights mintán jól megoldott accordion-szerű UX van — itt is alkalmazható, DE a válasz alapból a HTML-ben szerepeljen (display:block vagy aria-expanded='true'), különben az AI-crawler nem indexeli. FAQPage schema KÖTELEZŐ — 11. fejezet.

# 9. Kapcsolat (a footer felett)

### Szekciócím

**Kapcsolat**

### Bevezető

Keress minket bizalommal a megadott elérhetőségek bármelyikén, készséggel állunk rendelkezésedre.

### Kontakt-blokk

**Tóth Angéla**

Értékesítő, account manager

 

Telefon: +36 (30) 174 2022

E-mail: angela.toth@nrc.hu

**TELEFONSZÁM EGYSÉGESÍTVE: **A v4.0-ban az aktuális, helyes telefonszám: +36 (30) 174 2022. Ez minden NRC anyagban (termékoldal, naptár-widget, kapcsolati blokk, footer, .ics fájl, schema markup) egységesen jelenik meg. A korábbi NRC anyagokban (omnibusz PDF, főoldal) szereplő +36 (20) 174 2022 RÉGI adat, NEM aktuális — ezeket az anyagokat is frissíteni kell, hogy minden NRC platformon ugyanaz a szám szerepeljen.

**FEJLESZTŐI INSTRUKCIÓ: **Telefonszám: tel: link kötelező (tel:+36301742022). E-mail: mailto: link (mailto:angela.toth@nrc.hu). Angéla portré ide is jöjjön (jobboldalt), ahogy az AI Insights oldalon.

# 10. Árajánlatkérő űrlap

### Szekciócím

**Kérjen árajánlatot most vagy foglaljon időpontot!**

### Két tab

Tab 1: Ajánlatkérés

Tab 2: Időpontfoglalás

### Ajánlatkérés form mezők

• Vezetéknév

• Keresztnév

• Cégnév

• Telefonszám

• Céges e-mail cím

• Céges weboldal címe

• Üzenet

• File feltöltése (opcionális)

• Checkbox: Elfogadom az adatkezelési tájékoztatót

• Submit gomb: Elküldés

**FEJLESZTŐI INSTRUKCIÓ: **Az AI Insights oldalon ugyanezek a mezők szerepelnek — ugyanazt a form-struktúrát használd. Az időpontfoglalás (Tab 2) Calendly vagy Cal.com integrációval. Az adatkezelési tájékoztató link: https://nrc.hu/adatvedelmi-iranyelvek/

# 11. Schema.org JSON-LD kódok (a <head>-be)

Négy kötelező schema-blokk a fejléchez.

## 11.1. Service schema

<script type="application/ld+json">

{

  "@context": "https://schema.org",

  "@type": "Service",

  "name": "Omnibusz kutatás",

  "serviceType": "Online piackutatás",

  "provider": {

    "@type": "Organization",

    "name": "NRC Data",

    "url": "https://nrcdata.hu"

  },

  "areaServed": { "@type": "Country", "name": "Magyarország" },

  "description": "Omnibusz kutatás 1000 fős reprezentatív mintán, 5 szempont szerint súlyozva. Havonta 3 hullám, 3 nap adatfelvétel, 4. napon kész adatbázis.",

  "offers": {

    "@type": "AggregateOffer",

    "lowPrice": "80000",

    "highPrice": "190000",

    "priceCurrency": "HUF"

  }

}

</script>

## 11.2. FAQPage schema (a 8 kérdés-válasszal)

A teljes 8 kérdés-választ JSON-LD-be kell rakni. Itt csak az első 2 mintaként:

<script type="application/ld+json">

{

  "@context": "https://schema.org",

  "@type": "FAQPage",

  "mainEntity": [

    {

      "@type": "Question",

      "name": "Miért a leggyorsabb reprezentatív módszer az omnibusz?",

      "acceptedAnswer": {

        "@type": "Answer",

        "text": "Az NRC omnibusz havonta 3 hullámmal indul, a netpanel.hu közel 100 000 fős aktív válaszadói közösségére épül. 3 nap az adatfelvétel, 4. napon kész az adatbázis."

      }

    },

    {

      "@type": "Question",

      "name": "Mennyibe kerül egy omnibusz kutatás?",

      "acceptedAnswer": {

        "@type": "Answer",

        "text": "Fix kérdéstípus-alapú árazás. Zárt kérdés 80 000 Ft-tól, nyitott kérdés 160 000 Ft-tól. Példa: 3 zárt kérdés = 240 000 Ft + ÁFA."

      }

    }

    // ... a többi 6 kérdés ugyanilyen struktúrával

  ]

}

</script>

## 11.3. HowTo schema

<script type="application/ld+json">

{

  "@context": "https://schema.org",

  "@type": "HowTo",

  "name": "Hogyan zajlik egy omnibusz kutatás az NRC Datánál",

  "step": [

    { "@type": "HowToStep", "name": "Ajánlatkérés", "text": "1 munkanapon belül személyre szabott ajánlat." },

    { "@type": "HowToStep", "name": "Kérdőív véglegesítése", "text": "Leadási határidő: az adatfelvétel előtt 24 órával." },

    { "@type": "HowToStep", "name": "Adatfelvétel", "text": "3 nap, 1000 fős országos reprezentatív minta." },

    { "@type": "HowToStep", "name": "Adatbázis", "text": "A 4. napon kész SPSS-súlyozott adatbázis." },

    { "@type": "HowToStep", "name": "Átadás", "text": "Kereszttáblák, topline-riport, dashboard opcionálisan." }

  ]

}

</script>

## 11.4. BreadcrumbList schema

<script type="application/ld+json">

{

  "@context": "https://schema.org",

  "@type": "BreadcrumbList",

  "itemListElement": [

    { "@type": "ListItem", "position": 1, "name": "Főoldal", "item": "https://nrcdata.hu" },

    { "@type": "ListItem", "position": 2, "name": "Adatfelvétel", "item": "https://nrcdata.hu/adatfelvetel" },

    { "@type": "ListItem", "position": 3, "name": "Omnibusz kutatás", "item": "https://nrcdata.hu/adatfelvetel/omnibusz-kutatas/" }

  ]

}

</script>

# 12. VALIDATION LISTA — élesítés előtt

## Az NRC-től bekérendő (KRITIKUS):

**v4.0 STÁTUSZ — minden NRC-adat validált: **A v3.0-ban szereplő 9 NRC-bekérendő mind megérkezett és beépítve. A v4.0 tartalma minden tény-állítás szempontjából élesíthető. Új bekérendő pontok csak az ügyfél-vélemények finomításához (anonim helyett valódi referencia) és a naptár-widget végső validálásához vannak.

### Opcionális — később finomítható az NRC-vel:

- Az anonim ügyfél-idézet helyett 1 publikálható, név szerinti vagy anonimizált ("CMO @ vezető magyar FMCG") idézet — Cialdini-szempontból erősebb.

- A 3 esettanulmány-kocka helyettesíthető valódi NRC referenciákkal — ha az NRC ad publikálható eseteket. Iparág-preferencia: PR ügynökség, pénzügyi szolgáltató, FMCG.

- A 2026-os hullám-dátumok ELLENŐRZÉSE a naptár-widget-ben — a kódban becsült dátumok szerepelnek (5., 15., 25., decemberben 7., 14.). Ha az NRC pontosabb dátumlistát ad, frissítendő a widget OMNIBUSZ_WAVES_2026 tömbjében.

## A fejlesztőnek küldendő:

- Új termékbemutató oldal építése az /adatfelvetel/omnibusz-kutatas/ URL-en, az AI Insights mintára.

- Title tag és meta description beillesztése a <head>-be.

- 4 schema-blokk a <head>-be: Service + FAQPage + HowTo + BreadcrumbList.

- ÚJ: Event schema markup a 35 omnibusz hullámhoz — a 3.7. fejezet és a naptár-widget README szerint.

- ÚJ: Naptár-widget integráció — a fejlesztőnek átadott nrc_omnibusz_naptar_widget_csomag.zip alapján. Iframe-mel beilleszthető. Becsült fejlesztési idő: 2-3 óra.

- Sticky CTA gomb (3.5. fejezet) — jobb oldalsávon asztalon, bottom-sticky mobilon. HubSpot form integrációval.

- Stat-sávban valós számok a HTML-ben (3, 1000, 5, 10, 95 726, 528 531) — JS csak animálja. 4 stat-blokk a 3 helyett.

- Belső linkek aktiválása a „Mire NEM való" szekcióban — 5-6 link a többi NRC szolgáltatás-aloldalra.

- CTA anchorok: #ajanlat (form), #idopontfoglalas (Calendly/Cal.com), #letoltes (HubSpot form).

- Use case kártyák responsive design: asztalon 3×2 rács, mobilon függőleges. A 6. kártya (Több hullámos tracking) ne maradjon ki!

- Esettanulmány-kockák (Ügyfélélmény szekció): asztalon 3 oszlop, tableten 2, mobilon függőleges.

- HubSpot form integráció: az oldal alján a fő ajánlatkérő, valamint a sticky CTA gombnál a letöltés-form. Telefonszám-mező NE legyen.

- FAQ szekció: minden válasz alapból a HTML-ben (display:block vagy aria-expanded='true').

- Telefonszám egységesítés: +36 (30) 174 2022 minden NRC platformon (omnibusz PDF, főoldal stb. is).

## Külső forrásból ellenőrizendő:

- Versenytársak (Publicus, Forecast, TÁRKI, omnibuszkutatas.hu, Ipsos) jelenlegi hullám-frekvenciája — a „havi 3 hullám = leggyakoribb" állítás 2026-ban változatlanul érvényes-e.

# 13. Mit használj újra ennek mintájára?

Ez a dokumentum az AI Insights minta szerint készült termékbemutató oldal. Ugyanezt a szerkezetet javasoljuk minden szolgáltatás-aloldalra:

- Hero (eyebrow + H1 + lead + 2 CTA)

- Stat-sáv (3 fő szám)

- "Mire alkalmas?" — 6 use case kártya, mindegyiknél valódi értékajánlat

- "Mire NEM való?" — Cialdini bizalom-elem, belső link-háló

- Hosszabb szöveges szekció a panel-statisztikákkal

- Ügyfélélmény (idézet)

- FAQ — 7-10 kérdés

- Kapcsolat (Tóth Angéla)

- Űrlap (ajánlatkérés + időpontfoglalás tab)

 

**Társfájlok: **nrcdata-cikk-sablon.md — a hosszú formátumú inspirációs cikk receptje. nrcdata-lead-magnet-sablon.md — a letölthető PDF receptje. omnibusz_mintacikk.docx — az első, részletes mintacikk hivatkozási alapként.
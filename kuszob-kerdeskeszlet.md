# Küszöbmérő kérdéskészlet — eszkalációs threshold kalibrálásához

A cél nem a válaszminőség mérése, hanem annak megállapítása, hogy a
**legjobb rerank score** hol választja el az érdemben megválaszolható kérdéseket
a megválaszolhatatlanoktól. Ezért kellenek a határesetek is.

Futtatás: mind a négy kategória a teljes pipeline-on, a `top_rerank_score` rögzítésével.

---

## A / Erős pozitív — a tudásbázis közvetlenül tartalmazza

Elvárás: magas score, magabiztos válasz forrással.

1. Mikor indul a következő omnibusz?
2. Mennyibe kerül egy egyválaszos kérdés az omnibuszban?
3. Hány fős az omnibusz mintája és kikre reprezentatív?
4. Mennyi idő alatt kapom meg az adatokat, ha ma leadom a kérdést?
5. Mi a különbség az adatátadás és az elemzéssel csomag között?
6. Mikor van a kérdőív leadási határideje?
7. Milyen kedvezmény jár, ha tíz kérdést teszek fel?
8. Hogyan ellenőrzitek, hogy valódi válaszadók töltik ki a kérdőívet?

## B / Gyenge pozitív — közvetve válaszolható, de nincs szó szerinti forrás

Ez a legfontosabb kategória. Itt derül ki, hogy a küszöb nem vág-e le
olyan kérdéseket, amikre a rendszer még értelmes választ tudna adni.
Elvárás: közepes score, óvatosabb, de érdemi válasz.

9. Márkaismertséget szeretnék mérni, jó erre az omnibusz?
10. Öt kérdésem lenne, ebből kettő nyitott — nagyjából mennyi lesz?
11. Van olyan kutatásunk, ahol 300 fős célcsoportot kell elérni. Az omnibusz jó erre?
12. Kampány előtt és után is mérnék. Hogyan érdemes ezt időzíteni?
13. Mobilon is kitöltik a kérdőívet, vagy csak asztali gépen?
14. Nemzetközi adatfelvételre is van lehetőség?

## C / Negatív — a tudásbázis nem tartalmazza

Elvárás: alacsony score, a grounding-logika kimondja, hogy nincs forrás,
és eszkalál. Ha ezekre magabiztos választ ad, az hallucináció.

15. Hány éve alapították az NRC-t és ki a tulajdonos?
16. Milyen szoftverrel készítitek a súlyozást?
17. Mekkora az NRC éves árbevétele?
18. Milyen fizetési határidővel dolgoztok?
19. Ki a mi account managerünk?
20. Melyik versenytársatoknál olcsóbb az omnibusz?

## D / Szabály alapú eszkaláció — a score magas lehet, mégis emberhez megy

Ezek részben retrievable-ök, de a scope szerint eszkalálni kell.
Ez **nem** score-alapú döntés, hanem osztályozó: egyedi árazás,
kedvezmény, szerződéses vállalás.
Elvárás: a szabály elsüt a score-tól függetlenül.

21. Ez féléves trackingként kellene, három országban. Mennyi kedvezményt tudtok adni?
22. Ha éves keretszerződést kötünk, mennyivel megyünk lejjebb az árlistából?
23. Tudtok garantálni, hogy pénteken már nálam lesz az adat?
24. Aláírnátok egy titoktartási szerződést a kérdéseinkre?

---

## Amit a mérésből ki kell olvasni

Rendezd a huszonnégy kérdést a `top_rerank_score` szerint csökkenően, és nézd meg,
hol keverednek össze a kategóriák.

Ha az A és a C tisztán szétválik, a küszöb a kettő közé kerül. Ha a B kategória
belóg a C tartományba, akkor a küszöb túl agresszív lenne — inkább alacsonyabbra
kell tenni, és a bizonytalanságot a válasz szövegében jelezni, nem eszkalációval.

A küszöb megválasztásánál a **hamis negatív drágább**: az az eset, amikor a rendszer
egy megválaszolható kérdést is emberhez küld, csak kényelmetlen. Az ellenkezője —
amikor kitalál valamit — a demón és élesben is végzetes. Kétség esetén szigorúbb küszöb.

A D kategória nem befolyásolja a küszöböt. Ha a D-kérdések score-ja magas,
az rendben van: azokat nem a score, hanem a szabály fogja meg.

# Ipari-matek-2020

Alapvetően az első 4 feladat bonyolúltságukat tekintve egy main-ben fut (a teszt esetek), és külső file-okból importálva a konkrét feladatokat. (https://github.com/zsvizi/course-industrial-maths)

1. Feladat
  Az bal felső sarokból indulva kiszámoljuk a 2x2-es blokkok tartalmát, melyeket annak bal felső sarkába le is mentetjük, mivel azt már úgyse kell többször felhasználnunk. Ezt elvégezzük a 10x10-es mátrix első 9 sorára és oszlopára, így megkapjuk a kivánt eredményeket, de még benne van a mátrix 10-ik sora és oszlopa amiket törlünk.
 
2. Feladat
  For ciklussal ami végig megy a bemenő karakter listán, ha E-t láttunk a kezdeti pozicióból felfelé lépünk, stb... ezeket if-ekkel megvalósítva.

3. Feladat
  A random package használatával, a rand.choice lehetőséget ad, hogy egy másik lista elemeiből (itt [-1,1]) válasszunk megadható hosszú listát (itt 1000). Itt nem teljesen világos, hogy mit jelent a "szintén 100 elemű lista" (az első is 100 vagy a második 1000?), mindenesetre nálam a második 100 hosszú és az első pedig 1000. Létrehozva egy változót 0 kezdőértékkel, majd for ciklussal mindig az elözőhöz hozzáadva kaphatjuk az új elemet. Amit a matplotlib csomaggal ki is tudunk rajzolni. (Kicsit megtévesztő a "needed packages:" megnevezés, minta ténylegesen ez lenne a nevük :( )

4. Feladat
  a, A feladat nehézsége az volt, hogy valahogy kiválasszuk a 3 hosszú egymást követő elemeket a tömbből majd ezek között találni legalább egyet, ami mind a 3 helyen nagyobb, mint a határérték. Elöször mindegyikhez az igazságértéket rendeltem mindegyikhez aszerint,hogy meghaladják-e a küszübértéket (np.greater_equal). A problémát úgy oldottam meg, hogy az eredeti bemeneti tömbhöz hozzá adtam egy új sorban (np.vstack) az eredeti eggyel balra vett eltoltját, és még egy sort hozzáadtam csak 2-vel eltolva balra az eredetit, a végeket False-szal feltöltve (np.append), ekkor az oszlopaiban előálltak a 3 hosszú egymást követő tömbök, a végén nem állhat elő mind három helyen True, hisz a végeket False-szal bővítettük. Majd np.all(mátrix,axis=0)-val megnéztem minden oszlopra, hogy mi az igazságértéke (True,True,True->True), majd a np.any("all-lal létrejött tömb") megmondja, hogy van-e benne legalább egy True, amit vissza ad válaszként.
  
  1. 2. 3. ... (n-3). (n-2).  (n-1).
  2. 3. 4. ... (n-2). (n-1).  False
  3. 4. 5. ... (n-1).  False  False
  
  b, Az elözőekhez hasonlóan létrehozzuk a B=np.all(mátrix,axis=0) tömböt, majd ennek elemeit átírva int-ekre (False->0,True->1) ezt is eggyel balra eltolva B-hez adtam új sorként, végén 0-val bővítve*. Ekkor az oszlopban lévő két elemet összeszorozva megkapjuk, hol volt hosszabb fékezés (ez elözőhőz elég hasonló).
  
  Pl.:  0 0 1 1 1 0 1 0 1 1 1 -> 3 fékezés van benne, de ez még 7 fékezést lát
        0 1 1 1 0 1 0 1 1 1 0
        
       =0 0 1 1 0 0 0 0 1 1 0 -> 4 "egymást követő"/fékezés folytatási darab van
       
 Végül hogy megkapjuk a fékezések számát: np.sum(B)-np.sum("B keletkezett tömb", azaz az összes 3 hosszú fékezés-összes fékezés folytatás darab.

# Specifikacija projekta i FAQ

Tema projekta je vizualizacija struktura tipa grafa. Neophodno podržati više tipova izvora podata kao i njihovu
vizualizaciju. Ideja projekta je da naučite da koristite benefite objektog orijentisanog programiranja koji vam
omogućava da sa lakoćom menjate određene komponente vašeg softvera korišćenjem *plugin*-ova.

## 1. Arhitektura

Aplikacija treba da se sastoji od sledećih komponenti:

- **Platforma**: `Django` aplikacija koja sadrži glavne funkcionalnosti nad manipulacijom grafa i sprovodi
  komunikaciju između *plugin*-ova.
- **Plugin**:
    - **Data source plugin**: parsira određeni skup podataka i pri tome konstruiše graf (model podataka).
    - **Visualizer plugin**:  radi vizualiaciju modela podataka uz oslonac na `Django template`-a i `force-layout D3.js`
      biblioteku.
- **API**: `Python` biblioteka koja sadrži apstrakcije koji modeluju API (i sam model podataka) za`Data source`
  i `Visualizer` *plugin*-ova. Ova biblioteka se koristi kao *dependency* od strane platforme (koja koristi API) i
  svih *plugin*-ova (koji implemntiraju API). Takođe, kod je neophodno dokumentovati kako bi se olakšalo korišćenje same
  biblioteke. Ideja ove biblioteke je da olakša komunikaicju između *plugin*-ova i platforme i preporučuje se korišćenje
  `abs` i `typing` paketa. **Opciono**: verzionisanje biblioteke u skladu sa [Semantic Versioning](https://semver.org/).

Platformu i *plugin*-ove treba razviti kao komponente i instalirati ih u virtualno razvojno okruženje (`virtualenv`).
Ovakvom arhitekturom pored *plugin*-ova omogućavamo da se i sama platforma može lako promeniti kao komponenta npr.
prelazak sa `Django`-a na `FastAPI`.

Organizacija projekta treba da obuhvata sledeće foldere:

- `api`,
- `platform` (ima dependency na `api`),
- `data_source_plugin-1` (ima dependency na `api`),
- `data_source_plugin-2` (ima dependency na `api`),
- `simple_visualizer` (ima dependency na `api`),
- `block_visualizer` (ima dependency na `api`),
- `graph_explorer` (glavni projekat koji ima *dependency*-ije na platformu i sve *plugin*-e)

**Napomena**: Dodeliti smislene nazive `plugin`-ova.

## 2. Funkcionalnosti

### 2.1. Platforma

U aplikaciji **nije** potrebno implementirati sesiju niti prijavu i registraciju korisnika. Možete pretpostaviti da će
sa aplikacijom u datom trenutku komunicirati najviše jedan korisnik.

Model podataka treba omogući podršku **usmerenih**, **neusmerenih**, **acikličnih** i **cikličnih** grafova. Takođe,
model treba da podrži opciju da vrednosti mogu biti različitih tipova: `int`, `str`, `float`, `date`. **Nije**
dozvoljeno sve vrednosti čuvati kao `string`.

#### 2.1.1. Vizualizacija grafa

Platforma treba da omogući vizualizaciju grafa na 3 načina: `Tree View`, `Bird View`, `Main View`.

`Main View` (centralni prikaz grafa) predstavlja platno koje treba prikazati graf na 2 načina koristeći odgovarajuće
*plugin*-e za vizualizaciju ([Simple](#231-simple-visualizer), [Block](#232-block-visualizer)).
Neophodno je omogućiti operacije: `pan`, `zoom`, `drag and drop`, dobijanje detalja o tekućem objektu (`mouseover`).

`Tree View` (prikaz grafa u vidu stabla) omogućava akcije za dinamičko otvaranje i zatvaranja čvorova po uzoru na
*package explorer* poznatih integrisanih razvojnih okruženja (*IDE*). Graf se moze prikazati u formi teksta (npr.
*YAML*), korišćenjem grafičkih elemenata ili koristićenjem gotovih biblioteka za *package explorer*. Znak plus pored
objekta znači da se on može otvoriti/raširiti, dok minus znači da se objekat može zatvoriti/sakriti. Formiranje grana na
`Tree View` se vrši tako što se jedan čvor odabere kao koren (nasumično, ili na neki drugi način) i na osnovu njega se
formira ostatak grafa.

**Primer**: `Tree view` prikaz grafa u tekstualnom YAML formatu.

```json
{
  "id": "id1",
  "first": "John",
  "last": "Doe",
  "years": 53,
  "children": [
    {
      "id": "id2",
      "first": "Mike",
      "last": "Doe",
      "years": 25,
      "children": []
    },
    {
      "id": "id3",
      "first": "Lucy",
      "last": "Doe",
      "years": 15,
      "children": []
    }
  ]
}
```

![tree-view.png](.docs/tree-view.png)

`Bird View` (prikaz grafa iz ptičje perspektive) - umanjeni prikaz grafa koji u potpunosti mora stati u površ za
iscrtavanje.

`Bird View` treba da oslikava glavni prikaz (`Main View`) sa tom razlikom da ceo graf mora stati na platno predviđeno za
iscrvanje. Neophodno je pronaćo odgovarajući faktor skaliranje. Drugačije rečeno, to je prikaz grafa koji se već nalazi
na `Main View`-u, samo iz pričje perspektive. `Bird View` treba da obuhvati `viewport` (pravougaonik) koji se pomera u
skladu sa trenutnom prikazom na `Main View`. Ponašanje `viewport` je definisano na sledeći način:

- `zoom out` operacija na `Main View` treba da umanji `viewport` na `Bird View`-u u skladu sa određenim faktorom
  skaliranja.
- `zoom in` operacija na `Main View` treba da uveća `viewport` na `Bird View`-u u skladu sa određenim faktorom
  skaliranja.
- Sihronizacija sa pomeranjem prikaza na `Main View`.

Sva 3 prikaza grafa moraju da budu istovremeno dosputna i da određeni graf prikažu na 3 različita načina.
Prilikom selekcije čvora grafa na nekom od tri pomenuta prikaza, potrebno je da odgovarajući čvor dobije **fokus na sva
tri prikaza**.

Slika ispod prestavlja primer kako bi UI mogao da izgleda (ne morate te se striktno pridažavati ovog dizajna).
![img.png](.docs/app-ui.png)

> **Pitanje**: Ako postoji ciklus između čvora 1 i čvora 2, kako to prikazati u Tree View? Kako sprečiti
> rekurziju. <br/>
> **Odgovor**: Kad korisnik zatraži otvaranje čvora, dovući njegov sadržaj (ne morate slati poseban zahtev na server,
> dovoljno je iščitati iz nekog JS objekta) i dinamički napraviti HTML za njega. Sledi i prikaz TreeView. Pritiskom na
> plus bi se mogao dovući sadržaj.

![tree-view-recursion.png](.docs/tree-view-recursion.png)

> **Pitanje**: Da li Tree View i Bird View treba implementirati kao posebne plugin-e? <br/>
> **Odgovor**: Može, ali nije neophodno. Dovoljno je da budu deo *Django* aplikacije.

> **Napomena**: Upotreba `D3.js` biblioteke nije obavezna ali se preporucuje.

> **Pitanje**: Na koji način treba da se importuje `D3.js` biblioteka u naš projekat? <br/>
**Odgovor**: Ovo možete uraditi na dva načina. Prvi je da iz `src` atributa `script` taga direktno gađate zvaničnu
> stranicu `D3.js` biblioteke. Mana ovog načina je što možda neće dobro raditi ukoliko ste iza proxy-a. U tom slučaju bi
> najbolje bilo da prilikom odbrane koristite sopstveni hotspot. Drugi način jeste da preuzmete `D3.js` biblioteku i u
> projektu referencirate lokalnu kopiju (kao što je to urađeno na vežbama). U tom slučaju bi trebalo da u `.gitignore`
> stavite putanju do lokalne verzije biblioteke kako se ista ne bi pojavila na Vašem GitLab repozitorijumu i bespotrebno
> usporavala preuzimanja sadržaja sa istog.


> **Pitanje**: Kod main prikaza grafa, ukoliko imamo situaciju da postoji grana `A->B` i grana `B->A`, te grane će se na
> grafu preklopiti i videće se jedna linija. Da li je to problem ili možemo da ostavimo tako? <br/>
**Odgovor**: Ukoliko stignete (nakon što sve ostalo odraite), pokušajte da prilagodite ForceLayout da se povratne grane
> ne preklapaju.

#### 2.1.2. Pretraga i filtriranje grafa

**Pretragu** treba implementirati tako da omogući unos proizvoljnog teksta (upit). Na osnovu unetog upita formirati
podgraf trenutnog grafa čiji čvorovi sadrže (operacija *contains*) naziv atributa ili vrednost atributa koji
zadovoljavaju pomenuti upit.

**Fitriranje** treba implementirati tako što se upit za filter unosi u posebno tekstualno polje.
Format upita je sledećeg oblika:

```text
<naziv_atributa> <komparator> <vrednost_atributa>
```

Komparator može biti jedan od sledećih operatora: `==`,`>`,`>=`,`<`,`<=`,`!=`.
Nakon unosa filtera, potrebno je formirati podgraf trenutnog grafa čiji čvorovi sadrže atribut koji zadovoljavaju uneti
filter. Takođe prilikom korišćenja filtriranja, korisniku treba priazati grešku ukoliko je uneta vrednost
neodgovarajućeg tipa.

Neophodno je omogućiti sukcesivna primena filter, odnosno search operacije. <br/>
**Primer**: Prikazan je početni graf G1 nad kojim se primenjuje filter opeacija. Ona rezultuje podgrafom G2. Nad G2 može
se primeniti search koji rezultuje grafom G3. Nad G3 može se primeniti filter, koji rezultuju G4, itd. Način povratka na
inicijalni graf prepušten je studentima. Potrudite se da za to odaberete akciju koja je intuitivna korisniku.

> **Napomena**: Pretraga i filtriranje grafa je treba primeniti na `Main View`, `Tree View` i `Bird View`.

> **Napomena**: Nije dozvoljeno pretragu i filtriranje raditi u JavaScript-u na frontend-u.

> **Pitanje**: Da li je u redu da nakon izvršene pretrage ili filtriranja grafa, čvorovi koji odgovaraju unetim
> parametrima budu samo prikazani drugom bojom? <br/>
**Odgovor**: Ne! Potrebno je formirati podgraf shodno upitu unutar Core komponente, koji će
> odgovarajući plugin za vizuelizaciju prikazati.

> **Pitanje**: Imam pitanje u vezi filter opcije. Većina atributa u nasim izvorima su stringovi ili string
> reprezentacija brojeva. Kada radimo filter, da li da pokusamo prvo da ih parsiramo u int vrednost i tako poredimo
> poredbenim operatorima (`<`, `>`, `==`, ...) ili mozemo da ih poredimo sve leksikografski? <br/>
> **Odgovor**: Zadatak plugina za parsiranje je da podatke parsira u one tipove koje podaci predstavljaju. Svakako da
> treba posebno izdvojiti brojeve, datume, itd. u odgovarajuće tipove podataka. Filter primenjuje relaciju poretka u
> skladu sa tipom atributa.

#### 2.1.3. Čuvanje podataka (opciono)

Model grafa nakon parsiranja moguće je čuvati u bazi bilo kog tipa (preporuka: `Neo4j`). Takođe, dozvoljeno je čuvanje
na nivou instance klase naslednice `AppConfig` (pogledati način čuvanja *plugin*-a u primeru sa istih vežbi). Takođe,
dozvoljen i neki treći način uz prethodnu konsultaciju sa predmetnim asistentom.

> **Pitanje**: Kako mozemo menjati broj polja u django modelu posto imamo cvor koja sadrzi listu elemenata koja nije
> poznata na pocetku. <br/>
**Odgovor**: `Django model` je `ORMaper` za relacionu baze, i kao takav izmena šeme baze ili tabela nije nužno
> jednostavan proces. Morate unapred dobro izmodelovati vaše tabele, tako da mozete da pokrijete sve razlicite
> situacije, znači da napravite generički model i generičko rešenje. Ako ne želite da potrošite vreme na modelovanje,
> druga opcija je da nakon obrade source *plugin*-a radite migraciju. Poslednja opcija je da ne
> koristite `Django model`, nego da koristite `AppConfig` ili da koristite neku od *NoSQL* baza (`Neo4j`).

### 2.2. Data source plugin

Data source plugin treba da određeni izvor podataka parsira i formira graf (iz modela). Izvori podataka mogu biti bilo
koji podaci koji interno oslikavaja graf strukturu podataka (*JSON*, YAML, *XML*, *HTML*, *CSV*, *RDF*, *File System*,
šema relacije baze podataka itd.). Za parsiranje podataka možete koristiti već gotove parsere (za *JSON*, *XML*, *CSV*,
itd.) kao i ostale alate koji su vam neophodni. Podatke možete pronađi na internetu ili ih sami izgenerisati, ali je
neophodno obezbediti **minimum 200 čvorova grafa** i poželjno je da graf bude što veći.

Prilokom parsiranja određenog formata izvora podataka (npr. *JSON*), *plugin* treba da obezbedit parsiranje
**proizvoljnog** dokumenta tog formata i formiranje grafa na osnovu dokumenta. Formiranje grafa zavisi od konkretnog
dokumenta, ali evo nekih primera:

- **JSON**: objekti prestavljaju čvorove grafa, dok atribute i reference ka drugim objektima prestavljaju grane.
- **XML (HTML)**: Elemente *XML* dokumenta treba mapirati na čvorove grafa, dok atribute elemenata *XML* dokumenta
  treba mapirati na grane čvorova grafa. Tagove koji nemaju decu, posmatrati samo kao atribute, dok tagovi koji
  imaju podstablo, mogu se posmatrati kao čvorovi grafa.

*Plugin* mora da obezbedit parsiranje i formiranje **cikilčnog grafa** (model grafa mora da podržava ciklične
grafove). Određeni formati kao što je *RDF* podržavaju ciklične grafove i strukture, dok formati koji to ne podržavaju
moraju se nadograditi tako da obezbede ciklične strukture. Nadogradnja tih formata bi se svodala na uvođenje dodatke
semantike koja će omogućiti formiranje cikličnog grafa. *Plugin* i dalje treba da bude sposoban da parsira proizvoljan
dokument tog formata i da detektuje da li je u pitanju ciklična struktura. Ako je u pitanju aciklična struktura, ne
postoje nikakve pretpostavke i parsira se dokument u potpunosti. U slučaju da je ciklična, parsira se dokument u
potpunosti i time se formira stablo, zatim se primenjuje definisana semantika tako što će se ordređena polja, atributi
itd., tretirati na specifičan i zajedno sa već formiranim stablom koristiti za formiranje cikličnog grafa. Ispod se
nalaze neki primeri ubacivanja semantike za formiranje cikličnih struktura koje niste u obavezi da se pridržavate i
imate na rasploganju da osmislite svoju semantiku.

Primer cikličnog *JSON* dokumenta:

```js
const obj = {
    "name": "I'm parent",
}

obj.children = [
    {
        "name": "I'm first child",
        "parent": obj
    },
    {
        "name": "I'm second child",
        "parent": obj
    }
]
```

```json
{
  "@id": "28dddab1-4aa7-6e2b-b0b2-7ed9096aa9bc",
  "name": "I'm parent",
  "children": [
    {
      "@id": "6616c598-0a0a-8263-7a56-fb0c0e16225a",
      "name": "I'm first child",
      "parent": "28dddab1-4aa7-6e2b-b0b2-7ed9096aa9bc"
    },
    {
      "@id": "940e60e4-9497-7c0d-3467-297ff8bb9ef2",
      "name": "I'm second child",
      "parent": "28dddab1-4aa7-6e2b-b0b2-7ed9096aa9bc"
    }
  ]
}
```

Primer cikličnog *XML* dokumenta:

```xml

<com.example.Persons>
    <Person>
        <name>Alice</name>
        <address>
            <street>123 Main St</street>
            <owner>
                <!--Use XPath to reference Peter as owner-->
                <Person reference="../../../../Person[2]"/>
            </owner>
        </address>
    </Person>

    <Person>
        <name>Peter</name>
        <address>
            <street>456 Second St</street>
            <owner>
                <!--Use XPath to reference Alice as owner-->
                <Person reference="../../../../Person[1]"/>
            </owner>
        </address>
    </Person>
</com.example.Persons>

```

**Opciono:** Omogućiti kroz konfiguraciju *plugin*-a definisanje semantike formiranja cirkularnog grafa. U primeru
cirkularnog *JSON* dokumenta moglo bi se kroz konfiguraciju promeniti da se umesto `@id` atributa koristi `@ref` atribut
za formiranje cirkularnog grafa.

> **Napomena**: Na odbrani je neophodno demonstrirati rad sa acikličnim i cikličnim grafovima pa u skladu sa tim je
> neophodno pripremiti odgovrajuće podatke.

> **Napomena**: *RDF* se može reprezentovati u viže formata (*RDF-XML*, *Turtle*, itd.). U slučaju da ste se opredelili
> za *RDF-XML* format, samim tim ste se opredelili za *XML* format kao izvor podataka i morate da pružite podršku za
> parsiranje proizvoljnog *XML* fajla. U koliko ovo ne želite, morate koristiti neku drugu reprezentaciju *RDF-a* (npr.
*Turtle*).


> **Pitanje**: Da li je potrebno programski omogućiti izbor izvorišta podataka koji ima očekivani format zapisa (onakav
> kako to plugin očekuje)? <br/>
> **Odgovor**: Može, ali nije neophodno.

### 2.3. Visualizer plugin

*Visualizer plugin* treba da omogući vizualizaciju grafa u skladu sa određenim dizajnom. *Plugin* na osnovu grafa (iz
modela podataka) dobijenog od strane platforme generiše **string** reprezentaciju *HTML* tagova koji će predstavljati
graf. Tu **string** reprezentaciju neophodno je vratiti platformi koja će znati kako da prikaže taj graf na određenoj
*web* stranici. String reprezentaciju generisati ručno ili upotrebom neke biblioteke za generisanje *HTML template*-a (
npr. `jinja2`).

> **Napomena**: Sav statički sadržaj treba da se nalazi u platformi (*Django templates, CSS, JS*), kao i *Django views*.
> Plugin može sadržati *jinja2 template*-e ukoliko se oni koriste za generisanje *string*-a.

> **Pitanje**: Kako da *inplace*-ujemo string koji predstavlja *HTML* u *Django template* <br/>
> **Odgovor**: Pogledati [ovaj](https://stackoverflow.com/questions/17609822/insert-string-with-tags-in-django-template)
> meterijal.

Neophodno je Implementirati 2 *plugin*-a za vizualizaciju grafa: **simple** i **block**.

#### 2.3.1. Simple visualizer

Jednostavan prikaz služi da korisnika upozna sa strukturom grafa. Od informacije prikažite nešto što jedinstveno
određuje čvor grafa (id, naziv, itd.). Možete prikazati i nešto više informacije ukoliko smatrate da su posebno korisne
za jednostavan prikaz, ali težite da zaista bude jednostavan. Pojedinačan čvor grafa može prikazati u obliku
proizvoljnog jednostavnog grafičkog elemenata (krug, trouga, pravougaonik, ...)

Primer grafa:

```json
{
  "id": "id1",
  "first": "John",
  "last": "Doe",
  "years": 53,
  "children": [
    {
      "id": "id2",
      "first": "Mike",
      "last": "Doe",
      "years": 25,
      "children": []
    },
    {
      "id": "id3",
      "first": "Lucy",
      "last": "Doe",
      "years": 15,
      "children": []
    }
  ]
}
```

![simple-visualizer.png](.docs/simple-visualizer.png)

#### 2.3.2. Block visualizer

Prikazuje pojedinačan čvor grafa u obliku pravougaonika na kome je pored naziva potrebno ispisati atribute čvora.

Primer grafa:

```json
{
  "id": "id1",
  "first": "John",
  "last": "Doe",
  "years": 53,
  "children": [
    {
      "id": "id2",
      "first": "Mike",
      "last": "Doe",
      "years": 25,
      "children": []
    },
    {
      "id": "id3",
      "first": "Lucy",
      "last": "Doe",
      "years": 15,
      "children": []
    }
  ]
}
```

![block-visualizer.png](.docs/block-visualizer.png)

### 2.4. Komunikacija između platforme i plugin-ova

*Data source plugin* parsira izvorište podataka i na osnovu toga instancira klase modela kako bi napravio graf. Taj graf
prosleđuje platformi koja ga negde interno sačuva (npr. `AppConfig`, baza, itd). Nakon toga, platforma šalje
podatke *plugin*-u za vizualizaciju koji na osnovu njih gradi *HTML(+CSS+JS) DOM* stablo. Taj *HTML* se vraća platformi
koja ga umeće na odgovarajuće mesto trenutno prikazanog *Django template*-a.

Kada korisnik poželi da pretraži ili filtrira čvorove grafa, to radi platforma nad grafom koji je negde prethodno
perzistirala (videti prethodni pasus). Rezultat ove operacije je podgraf koji se šalje *visualizer plugin*-u, koji
ponovo gradi *HTML DOM* stablo. Ono biva vraćeno platformi i umetnutno u *template*.

## 3. Realizacija projekta

### 3.1. Raspodela posla

Neophodno je implementirati platformu i minimalno 4 *plugin*-a, ukoliko tim broji 3 ili 4 člana. Ukoliko je tim
sastavljen od 5 studenata, tada je potrebno razviti 5 *plugin*-a. Svaki od članova tima mora razviti minimalno jedan
plugin. Broj *Visualizer plugin*-a je 2, dok je broj *Data source plugin*-a je 2, odnosno 3.

> **Pitanje**: Da li je u redu da izvorišta podataka budu dva dokumenta istog tipa (npr. *JSON*), koji sadrže različite
> podatke (npr. jedan sadrži informacije o avio-linijama, dok drugi sadrži informacije o društvenim mrežama). <br/>
> **Odgovor**: Ne!

> **Pitanje**: Šta ako implementiramo sve obavezne funkcije, ali posao nije ravnopravno podeljen? <br/>
> **Odgovor**: Na [adresi](https://www.igordejanovic.net/courses/sok/00-upoznavanje/) (slide 11), se nalazi spisak
> obaveznih operacija koje treba implementirati. Ako implementirate sve obavezne operacije, ispod njih imate
> opcione/dodatne operacije koje možete implementirati.

> **Pitanje**: Ako implementiramo neku od opcionih/dodatnih operacija, da li to može da zameni neku od obaveznih
> operacija (džoker)? <br/>
**Odgovor**: Ne! Operacije koje su specificirane su obavezne operacije. Operacije koje su specificirane pod opcione
> služe isključivo ako bude studenata zainteresovanih za dodatno zalaganje na predmetu, a koiji su pri tom
> implementirali sve obavezne operacije, i žele/mogu/hoće da urade više.

> **Pitanje**: Da li je moguće da u istom timu budu članovi koji imaju različite ambicije prema broju bodova? Na primer
> jedan član tima želi da radi za ocenu 10, a drugi za ocenu 8. Da li će to uticati na broj bodova, ili se svačiji rad
> ocenjuje zasebno? <br/>
**Odgovor**: Na projektu se pored saradnje studenata gleda i pojedinačno zalaganje. Neretko se dešavalo da studenti
> dobiju različit broj bodova shodno zalaganju.

> **Pitanje**: Dodeljen nam je još jedan kolega u tim i sad imamo tim od 5 članova. Sada je teže ukombinovati
> međusobno rad i teže zbog veće količine rada koji projekat nosi sa 5. članom. Šta raditi ukoliko neki od članova neće
> da sarađuje? <br/>
**Odgovor**: Što se izrade projekta tiče, ništa nije teže za petočlane timove. Core aplikacije ćete podeliti na 5
> delova (manje posla po čoveku), a svaki od članova razvija po jedan plugin. Napomenuo bih da se ocena dobija
> pojedinačno. Ako neko od članova pak odbije saradnju, broj plugina će se smanjiti za jedan. Na kraju svako od
> studenata treba da razvije tačno jedan plugin. Funkcionalnosti Core aplikacije se ne skaliraju (već dele na članove
> koji “žele” da rade).

### 3.2. Primena obrazaca

Primena obrazaca je obavezna i treba ih korektno primeniti na određenim problemima. Ne pokušavati na silu uglaviti
obrazac jer to zapravo predstavlja anti obrazac. Preporuka je implementirate kompletan projekat i tada probati da
sagledate probleme na koje ste nailazili prilikom realizacije projekta i razmisliti o primeni obrasca. Nije unapred
defnisan minimalni broj obrazaca koji je neophodno primeniti u projektu da ih ne biste forsirali na mestima tamo gde
nema smisla. Primena obazaca u projektu će se diskutovati na odbrani projekta.

### 3.3. Git

Neophodno je na nivou tima kreirati `GitLab` ili `GitHub` repozitorijum (ostali `git` provider-i nisu dozvoljeni za
korišćenje).

Git repozitorijum voditi po
preporučenom [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) modelu. Potrebno je
da da imate develop granu na kojoj se nalazi kod koji se intenzivno razvija i koji često testiraju svi članovi tima. Kod
na ovoj grani mora da radi, a čine ga do datog trenutka implementirane funkcionalnosti koje su dovoljno dobro
istestirane.

Razvoj nove funkcionalnosti radi se na posebnoj *feature* grani. Svaka feature grana odgovara tačno jednom *GitHub
issue*-u. Ove grane predstavljaju alternativne tokove razvoja. Jednu funkcionalnost radi jedan student. Kada se
funkcionalnost završi, potrebno je ovu granu spojiti sa *develop* granom putem *merge request*-a (*pull request*-a).
*Feature* grane imenovati u formatu `feature-<naziv_grane>`.

U slučaju da primetite neki *bug*, tada pronalazite *issue* koji odgovara funkcionalnosti, ponovo ga otvarate i kreirate
odgovarajući *bugfix* granu (format imenovanja je `bugfix-<naziv_grane>`). Na njoj popravljate bug i radite inicijalno
testiranje. Kada ste utvrdili da je problem otklonjen, kod spajate sa *develop* granom putem *merge request*-a (*pull
request*-a).

Periodično, kod sa *develop* grane prebacujete na *master* granu. *Master* treba da ima stabilnu verziju projekta i
*merge* na *master* grani će se raditi samo prilikom implementacije *milestone*-a, odnosno kada završite kontrolnu tačku
ili projekat.

*Milestone* oslikava jedan bitan momenat životnog ciklusa vaše aplikacije. Što se tiče ovog projekta možete da
imate 2-3 *milestone*-a. Rokovi su: I kontrolna tačka, (eventualno II kontrolna tačka) i Predaja projekta (biće naknadno
specificirani u dogovoru sa profesorom). *Milestone* sadrži *task*-ove (*GitLab issues*), koji su implementirani tokom
tog *milestone*-a.

Jedan *task* treba da se odnosi na jednu funkcionalnost aplikacije (engl. *feature*), koja će biti razvijena na
posebnoj *feature* grani. *Task*-ove je potrebno napraviti unapred za *milestone* koji je u toku. Zatim, svaki student
uzima *task* po *task* (dodeljuje mu se *issue*), te započinje implementaciju odgovarajuće funkcionalnosti. Kada se
implementacija funkcionalnosti završi i uspešno odradi inicijalno testiranje, task se zatvara, a kod prebacuje na
*develop* granu. Nakon toga, ostale kolege treba da urade testiranje svih funkcionalnosti. Ukoliko se ustanovi problem u
nekoj od njih, potrebno je ponovo otvoriti odgovarajući task (ne praviti nov).

**Sve commit poruke moraju početi sa `#jedinstveni-identifikator-issue` kako bi se referencirao issue na koga se
commit odnosi**.

Grane *feature* i *bugfix* možete brisati radi preglednosti.

> **Pitanje**: Da li korstiti labele prilikom rada sa *GitLab issue*-ima? <br/>
> **Odgovor**: Da. Možete iskoristiti predefinisani skup labela.

> **Pitanje**: Na koji način zatvoriti *GitLab issue*? <br/>
> **Odgovor**: Direktno putem *GitLab*-a ili indirektno kroz poruku *commit*-a.

> **Pitanje**: Da li je potrebno da imamo tagove u našem repo-u? <br/>
> **Odgovor**: Nema potrebe i nije obavezno. Ako neko ipak želi, može tagovati verziju sa komoj ćete braniti projekat.

> **Pitanje**: Da li je moguće commit naknadno povezati sa Issueom? Napravila sam issue i commitovala medjutim nisam id
> issue-a ubacila u komentar nego van njega pa se nije povezalo. <br/>
> **Odgovor**: koristiti `git rebase` za izmenu sadržaja *commit*-a.

> **Pitanje**: Da li je bitan procenat završenosti milestone? <br/>
> **Odgovor**: Da! Težite da do krajnjeg roka milestone procenat završenosti tog milestone bude 100%. U tom slučaju se
> milestone smatra uspešnim. U suprotnom, došlo je do probijanja roka.

> **Pitanje**: Da li u istoriji izmena smeju da se nađu izmene nekoga van članova tima? <br/>
> **Odgovor**: Ne, u istoriji izmena ne treba da se nalaze izmene nikog sem članova vašeg tima. Ako morate da radite na
> tuđoj mašini iz bilo kog razloga onda podesite git config. Primer možete
> videti [ovde](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config). Ako se nađu izmene van
> članova tima, nema nikakve garancije da taj neko nije radio za vas.

> **Pitanje**: Rečeno je da svi članovi tima treba rade na platformi. Na gitlabu nije moguće dodeliti issue svim
> članovima tima, već samo jednoj osobi. Šta u tom slučaju da radimo? Da li da issue ostavimo unassigned? <br/>
> **Odgovor**: Odraditi finu granulacija issue-a, tj. raščlaniti ga na manje (atomične) issue-e, koje ćete dodeliti
> pojedinačnim članovima tima.

> **Pitanje**: Ako želimo da napravimo neku sitnu izmenu na komponenti nakon merge-a feature grane sa develop
> granom, a nije bug u pitanju, kako da nazovemo novu granu na kojoj ćemo praviti izmenu? Ili ponovo da iskoristimo
> feature granu koju smo koristili za razvoj komponente ali ne znam koliko je to dobra praksa? <br/>
> **Odgovor**: Upotrebom stare feature grana dolazite u situaciju da radite merge develop grane u pomenutu feature
> granu, što svakako nije dobra praksa. Bolje napraviti novu granu koja će se zvati isto kao feature grana, s tom
> razlikom da će imati prefiks/sufiks *enhancement* ili sl.

### 3.4. Podešavanje projekta

Repozitorijum treba da sadrži `README.md` datoteku u kojoj je naznačeno:

- Tim i članovi tima.
- Upustvo za instalaciju komponenti i parametrizaciju projekta (`Django` aplikacije i *plugin*-a).

**Opciono**: kreirati `Python`/`bat`/`bash` skriptu koja će da vrši instalaciju komponenti i podešavanje projekta.

> **Pitanje**: Da li možemo pretpostaviti da će se projekat pokretati u `PyCharm`-u te da iz tog razloga samo objasnimo
> parametrizovanje i podešavanje projekta kroz pokretanje u `PyCharm`-u ili je potrebno da napišemo i podešavanje kroz
> komandnu liniju? <br/>
**Odgovor**: S obzirom na to da su referentni primeri sa vežbi pokretani u terminalu, od Vas se može očekivati isto.
> Tako da je moj savet napraviti uputstvo po uzoru na uputstva sa vežbi.

> **Pitanje**: Prilikom izmene `views.py` fajla u platform komponenti i njegove ponovne instalacije, ove promene se
> nekad nasumicno ne azuriraju u `venv-lib-sitepackages-core`, tako da dobijam da se pokreće stariji kod, čak i nakon
> ponovne instalacija izmenjene platform komponente. Da li znate kako je moguce *refresh*-ovati ove fajlove tako da se
> izmene nastale u komponenti pojave i tu? Takođe, koja je neka preporučena način za razvoj komponentnih aplikacija, sa
> obzirom na činjenicu da se pri svakoj promeni mora izvršiti ponovna instalacija? U našem projektu je i platforma jedan
> komponenta, u kojem je `Django` aplikacija (po uzoru na vezbe). Pri svakoj izmeni u ovim komponentama moram opet
> raditi instalaciju pa pokretati server, što znatno otežava rad i dugo traje, ali drugačije **ne registruje** promene.
> Da li stvarno jedini način? <br/>
**Odgovor**: Preporuka je napisati skriptu (`shell`, `bat`, `python`, `perl`, itd.) koja bi odradila sav dodatan posao
> za Vas. Njen zadatak bi otprilike bio da odradi sledeće:
> - Iz razvojnog okruženja izbrisati sve instalirane komponente, njihove build direktorijume, itd.
> - Ponovno instalirati komponente u razvojno okruženje.
> - Pokrenuti server.

> **Pitanje**: Pošto se u projektu traži postojanje virtuelnog environment-a, kako da se on deli kroz git, pošto se u
> fajlu venv/pyvenv.cfg nalaze apsolutne putanje do python-vezanih stvari za instalaciju, one osobe koja je kreirala taj
> virtual environment, a nije praktično da svaki put menjamo putanju do naše instalacije pythona (i ostalih
> python-vezanih stvari). <br/>
> **Odgovor**: Svako od Vas treba da ima posebno okruženje koje se ne stavlja na git. Na git stavite `requirements.txt`
> fajl u kome ćete čuvati verzije neophodnih paketa. Više informacija možete
> pronaći [ovde](https://note.nkmk.me/en/python-pip-install-requirements/).

### 3.5. Dijagram klasa

Repozitorijum treba da sadži dijagram klasa u vidu slike, *PDF* ili *Markdown* dokumenta. Dijagram minimalno treba da
obuhvati klase koje čine model grafa, kao i “servisne” klase koje koristite u pluginima za učitavanje i vizualizaciju.
Za kreiranje dijagrama možete koristiti `PlantUML` ili [draw.io](https://app.diagrams.net/).

### 3.6. Kontrolna tacka

Asistent će odabrati nekoliko timova koji treba da ukratko prezentuju (10-15 minuta) šta su do datog trenutka odradili.
Prilikom prezentacije, osvrnuti se na sledeće:

- Šta je odrađeno?
- Zanimljivi problemi sa kojima ste se susreli?
- Kakav je plan za dalje?
- Nedoumice za nastavak izrade?

Kontrolna tačka ne nosi bodove.

### 3.7. Odbrana projekta

Održavaju se 3 termina odbrane projekta:

1. Janurasko-februarskom ispitnom roku (max 60 bodova).
2. Junsko-julskom roku (osvojenih bodovi se skaliraju sa 0.9).
3. Avgustovsko-septembarskom roku (osvojeni bodovi se skaliraju sa 0.8).
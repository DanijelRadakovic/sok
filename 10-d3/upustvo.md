# D3 biblioteka za vizualizaciju

> **Napomena**: Video-materijale za današnji termin vežbi možete
> pronaći [ovde](https://drive.google.com/file/d/1usVK8My45GlhoEvKsZiSlJxnH1YDrY4K/view?usp=sharing).

## Struktura projekta

Struktura priloženog `prodavnice` direktorijuma je sledeća:

- `django_project` direktorijum sadrži podešavanja *Django* veb sajta.
- `D3Core` direktorijum predstavlja plugin/komponentu koja se odnosi na *Django* aplikaciju. Ova aplikacija sadrži
  primere upotrebe `D3.js` biblioteke.
- `UcitavanjeKod` direktorijum predstavlja plugin/komponentu koja upisujue podatke u bazu podataka.

## Pokretanje projekta

Da biste pokrenuli projekat, potrebno je da u virtualno razvojno okruženje instalirate navedene plugine/komponente. To
radite na sledeći način:

```shell
cd prodavnice
# instalacija D3Core komponente
pip install ./D3Core
# instalacija UcitavanjeKod komponente.
pip install ./UcitavanjeKod

# pokretanje migracija i servera
cd django_project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

> **Napomena**: Moguće je jednostavnije pokrenuti aplikaciju putem skripte `run.sh`. Upotreba ove skripte moguća je na
> Linux OS-u. Uklanjanje generisanih datoteka i direktorijuma moguće je upotrebom `clean.sh` skripte.

## Ucitavanje plugina u Django aplikaciju

Plugin `UcitavanjeKod` implementira servis `UcitavanjeKod.ucitavanje.kod.ucitavanje_kod.UcitatiProdavniceKod` koji
redefniše apstraktnu klasu `D3Core.d3_primeri.services.ucitati.UcitatiService`. Kao što se može primetiti, ovaj plugin
upisuje podatke u bazu podataka `D3Core` *Django* aplikacije. Do učitavanja ovog plugina dolazi prilikom
startovanja `D3Core` *Django* aplikacije kada se izvrši `ready` metoda `AppConfig` klase naslednice. Više informacija u
kodu. Upotreba ovog plugina se demonstrira gađanjem sledećeg `endpoint`-a: `/ucitavanje/plugin/ucitati_prodavnice_kod`.
Vise informacija o tome šta se dalje dešava, pogledati kod i odgovarajuće komentare.

## D3.js

`D3Core` predstavlja *Django* aplikaciju koja je razvijena kao posebna komponenta (plugin za `django_project` sajt).
Pogledati kako izgleda njena`setup.py` skripta. Može se primetiti da nema `entry_points`, a Django ipak zna da je
prepozna. Takođe, pogledati kako se statički sadržaj instalira u paket (`package_data`). Ova aplikacija sadrži primere
upotrebe [D3.js](https://d3js.org/) biblioteke. Uvod u priču o ovom biblioteci možete pronaći na
profesorovim [predavanjima](http://www.igordejanovic.net/courses/tech/d3). Da biste koristili ovu biblioteku, neophodno
je njeno ucitavanje u `Django template` što mošete videti u `base.html` *template*-u.

### Primer 1

*Template* za ovaj primer je `primer1.html`, koji demonstrira upotrebu `svg`
elemenata. Potrebno je napraviti inicijalni `<svg>` element koji predstavlja
platno za iscrtavanje elemenata poput: kruga, pravougaonika, elipse, linije,
izlomljene linije, poligona, itd. Elemente možete grupisati
upotrebom [<g>](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/g) taga.
U *template*-u možete videti koje sve atribute `svg` elementi poseduje
i kako se njima može statički manipulisati.

### Primer 2

U `primer2.html` može se videti upotreba
[transform](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform) atributa za
transliranje `svg` elemenata.

### Primer 3

U `primer2.html` može se vidite upotreba
[transform](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/transform) atributa za transliranje
i skaliranje `svg` elemenata.

### Primer 4

U `primer4.html` koristi osnovne koncepte `D3.js` biblioteke za manipulaciju
*HTML* elementima. Više informacije možete pronaći u kodu i odgovarjućim komentarima.

### Primer Pan Zoom

Pogledati na koji način je moguće implementirati `Pan` i `Zoom` operacije (`primerPanZoom.html`).

### Primer Tree Layout

Pogledati na koji je način moguće podatke prikazati u obliku stabla (`primerProdavnicaTreeLayout.html`).

### Primer Force Layout

Pogledati na koji je način moguće prikazati podatke upotrebom `Force Layout`-a (`primerProdavnicaForceLayout.html`).

## Zadaci za vežbanje

Nakon upoznavanja sa `D3.js` bibliotekom neophodno je rešiti [zadatake](zadaci.md). Rešenja zadataka su dostupna
u `prodavniceResenje.zip` arhivi.
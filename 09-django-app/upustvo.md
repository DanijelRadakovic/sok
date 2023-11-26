# Django radni okvir

> **Napomena 1**: Ovaj dokument pretpostavlja da ste prethodno prošli
> kroz [Django tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/).

> **Napomena 2**: Video-materijale za ovaj termin vežbi možete pronaći
[ovde](https://drive.google.com/file/d/1M58H_HgpgMzDBokurFNZtqnAesMrN-xz/view?usp=sharing).

## Primer jednostavnog Django projekta

U priloženom direktorijumu `prodavnica` možete pronaći primer jednostavnog `Django`projekta. Prilikom upoznavanje sa
projektom obratiti pažnju na sledeće:

- Pogledati `README.txt` dokument i uz pomoć istog pripemiti bazu, kreirati admin korisnika, pokrenuti server.
- Pogledati kako se koristi admin aplikacija.
- Pogledati kako se koristi aplikaciju o prodavnicama.
- Upoznati se sa sadržajem `prodavnicesajt` direktorijuma:
  - podešavanje sajta (`settings.py`):
    - INSTALLED_APPS,
    - DATABASES,
    - ROOT_URLCONF,
    - STATIC_URL,
  - globalnim mapiranjem url putanja (`urls.py`).
- Upoznati se sa sadroajem `prodavnice` direktorijuma:
  - konfiguracija aplikacije `apps.py` i `AppConfig`,
  - model aplikacije (`models.py`).
- Način na koji se definiše nova `manage.py` komanda `(management/commands/popuni_bazu.py)` kao i način ažuriranja baze.
- `admin.py` i način uvođenja tabela (klasa) modela u admin sistem
- lokalnim `URL`-ovima i mapiranjem na `view`-ove (`urls.py`). Posebno obratiti paonju na imena `URL`-ova i `pattern`-e
- Definisanje `view`-ova i obrada zahteva:
  - `views.py`
  - `artikli_view.py`,
  - `prodavnica_view.py`.
  - Kako se u `view`-u dobavljaju informacije o metodi (naziv metode, parametri, itd.)
  - Povezivanje `view`-a i `template`-a.
  - CRUD operacije na prodavnicama.
- hostovanje statičkog sadržaja (`static` folder).
- `Django templates` u istoimenom folderu:
  - `base.html`:
    - Učitavanje statičkog sadržaja.
    - Relativno referenciranje `URL`-ova.
    - Blokovi.
  - `lista_prodavnice.html`
    - Kako se vrši nasleđivanje `template` i implementacija bloka.
    - Kako se koriste `Django` tagovi (`{% something %}`).

## Zadaci za rad
Nakon upoznavanja sa `Django` projektom, proširiti ga implementacijom na osnovu definisanih [zadataka](zadaci.md).
Rešenja zadataka dostupna su u `prodavnicaResenje.zip` arhivi.
# Virtualenv, venv i pip

Preporuka je da `Python3* interpreter koristite unutar virtualnog okruženja kojim ćete
upravljati upotrebom nekog od sledeća dva alata:

- [*virtualenv*](https://virtualenv.pypa.io/en/latest/)
- [*venv*](https://docs.python.org/3/library/venv.html).

## virtualenv

### Instalacija

```shell
pip install virtualenv
```

### Upotreba

Nakon instalacije, ne bi bilo loše proveriti da li `virtualenv` funkcioniše.
To možete uraditi na sledeći način. Otvorite komandnu liniju i otkucajte sledeću komandu:

```shell
virtualenv --version
```

Ukoliko je instalacija uspešna, trebalo bi da se prikaže instalirana verzija.

Da biste kreirali novo razvojno okruženje sa imenom `test-virt`, otkucajte sledeću komandu:

```shell
virtualenv test-virt
```

Da biste aktivirali kreirano virtualno okruženje, morate izršiti `test-virt/bin/activate`
skriptu.

```shell
source test-virt/bin/activate
```

Ukoliko proverite verziju *Python*-a koji koristite, trebalo bi da Vam se prikaže interpreter
virtualnog okruženja

```shell
which python3
# Output: $PWD/test-virt/bin/python3
#
# Note: $PWD represents the path of working directory
# Note: line that starts with '#' is bash comment. 
#       Don not expect to see '#' in the output.
```

Da biste deaktivirali razvojno okruženje, potrebno je izvršiti komandu `deactivate`
Ukoliko sada proverite koju verziju *Python*-a koristite, trebalo bi da vidite
sistemski interpreter.

```shell
which python3
# Output: /usr/bin/python3
```

## venv

### Instalacija

`venv` bi trebalo da je instaliran kao jedan od standardnih modula sistemskog *python3* interpretera.
Drugačije rečeno, instaliranjem `python3` interpretera na Vaš sistem, *venv* bi trebalo automatski da se instalira.

Na pojedinim operativnim sistemima, potrebno je odradite dodatna podešavanja.
Npr. na *Ubuntu/Debian* sistemima možda morate dodatno instalirati
[python3-venv](https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-ubuntu-18-04/) paket.

### Upotreba

Kreiranje virtualnog okruženja `test-virt`

```shell
python3 -m venv test-virt
```

Aktivacija i deaktivacija virtualnog okruženja se vrši na identičan način kao prilikom upotrebe
alata *virtualenv*.

## Alat pip

### Instalacija

Uputstvo za instalaciju (i korišćenje) možete pronaći na nekom od sledeća dva linka:

- [https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
- [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

### Upotreba

Ovaj alat koristimo za manipulaciju Python modulima unutar prethodno **aktiviranog virtualnog** okruženja.

**Napomena:** Nije pametno da menjamo module sistemskog interpretera.

Izlistavanje instaliranih python modula:

```shell
pip list
#  Output: 
#  Package       Version
#  ------------- -------
#  pip           20.3.4
#  pkg-resources 0.0.0
#  setuptools    44.1.1
#
#  Note: '#' is the comment in bash, ignore it.
```

Instaliranje novog modula (*Django* u ovom slučaju) obavlja se na sledeći način:

```shell
pip install Django
```

Provera da li je *Django* modul instaliran (mogu se primetiti i ostali propratni moduli
koje *Django* zahteva):

```shell
pip list

#  Package       Version
#  ------------- -------
#  asgiref       3.4.1
#  Django        3.2.8
#  pip           20.3.4
#  pkg-resources 0.0.0
#  pytz          2021.3
#  setuptools    44.1.1
#  sqlparse      0.4.2
```

Brisanje postojećeg `Django` modula iz virtualnog okruženja vrši se na sledeći način

```shell
pip uninstall Django
```

## Korisni linkovi i dokumentacija

U slučaju nekih poteškoća prilikom upotrebe opisanih alata ili slučaju da jednostavno
želite da saznate više o istim, korisno je upoznati se detaljnije sa sledećom
dokumentacijom:

- [*virtualenv*](https://virtualenv.pypa.io/en/latest/)
- [*venv*](https://docs.python.org/3/library/venv.html)
- [*pip*](https://pip.pypa.io/en/stable/)

### Napomena

Ovaj dokument pretpostavlja da koristite *Linux* operativni sistema.
U slučaju upotrebe drugog OS-a, konsultovati odgovarajuću dokumentaciju ili [google.com](https://www.google.com/).


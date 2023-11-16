# Dependency Injection

Današnji termin vežbi namenjen je za vežbanje `Dependency Injection`koncepta. Ovaj koncept služi za kreiranje objekata
koji formiraju složeni graf zavisnosti. Cilj upotrebe ovog koncepta jeste smanjenje nepotrebnog koda za inicijalizaciju
objekata.

Tokom ovih vežbi, koristićemo `Injector` biblioteku. Instalaciju iste u vaše virtuelno možete obaviti komandom:

```shell
pip install injector
```

Arhiva `DIExample.zip` sadroi `simple.py` modul u kome se nalazi jednostavan primer upotrebe ovog koncepta. Nešto
složeniji primer upotrebe se nalazi u modulu `injector_shops.py`.

Rešiti [zadatke](zadaci.md) korististeći smernice za njihovo rešavanje:

- Kostur za rešenje zadataka možete pronaći u `Vezbe5DIDemo.zip` arhivi.
- Prvi zadatak ne morate rešiti upotrebom `AbstractFactory` šablona.
- Za `inject`-ovanje klasa koje su `Singleton`, pogledati [dokumentaciju](https://injector.readthedocs.io/en/latest/scopes.html#singletons).
- U drugom zadatku potrebno je koristiti `CallableProvider`, čiji je primer upotrebe dostupan
  na [linku](https://injector.readthedocs.io/en/latest/api.html#injector.CallableProvider).
- Treći zadatak nije obavezan za rešavanje.
- Rešenje zadataka možete pronaći u `Vezbe5DIResenje.zip` arhivi.
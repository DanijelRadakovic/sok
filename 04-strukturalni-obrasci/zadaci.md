# Strukturalni obrasci - zadaci za vežbanje

## Zadatak 1

**Proxy Profiler**

Data je servisna klasa sa odred̄enim brojem metoda. Korišćenjem *Proxy* obrasca napraviti brojač poziva svake metode
klase `Service` kao i ukupno i prosečno vreme provedeno u svakoj metodi.

```python
from abc import ABC, abstractmethod


class Service(ABC):

    @abstractmethod
    def video360(self):
        pass

    @abstractmethod
    def video720(self):
        pass

    @abstractmethod
    def videoHD(self):
        pass


class VideoService(Service):
    """
    Real service implementation.
    """
    # TODO: implement constructor ...
    # TODO: each method should print the name and sleep for some time.
    pass
```

Kao primer definisati klasu `VideoServiceProxy` koji će za metode klase `VideoService` izračunati ukupan broj poziva
svake metode i prosečno vreme provedeno u svakoj metodi.

Pogledati:

- [PEP 418](https://www.python.org/dev/peps/pep-0418/#abstract).
- [High resolution time measurement](https://www.daniweb.com/programming/software-development/code/465991/high-resolution-time-measurement-python).

Za rešavanje se može koristiti funkcija `perf_counter()`. Za zaustavljanje izvršavanja može se pozvati
funkcija `sleep()` iz modula `time`.

## Zadatak 2

**Lazy Initialization Proxy**

Napraviti kasnu inicijalizaciju servisa koji zahteva dugo vreme inicijalizacije. Ispisima na konzoli prikazati redosled
instanciranja objekata i poziva metoda. Obezbediti da se inicijalizacija objekta izvrši kada klijent zahteva usluge
servisa. Kao primer definisati klasu `VideoProxy` koja ima metodu `play`. Prilikom poziva `play` metode, koristeći kasnu
inicijalizaciju, instancirati objekte klasa `VideoHD`, `Video360p` ili `Video720p` u zavisnosti od tipa videa koji se
pušta i pozvati `play` metodu odgovarajuće klase.
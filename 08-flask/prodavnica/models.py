class Prodavnica:
    def __init__(self, pib, naziv, adresa, broj_telefona):
        self.pib = pib
        self.naziv = naziv
        self.adresa = adresa
        self.broj_telefona = broj_telefona

    def __str__(self):
        return self.naziv


class Kategorija:
    def __init__(self, oznaka, naziv):
        self.oznaka = oznaka
        self.naziv = naziv

    def __str__(self):
        return self.naziv


class Artikal:
    def __init__(self, oznaka, naziv, opis, cena, na_akciji, prodavnica, kategorije):
        self.oznaka = oznaka
        self.naziv = naziv
        self.opis = opis
        self.cena = cena
        self.na_akciji = na_akciji
        self.prodavnica = prodavnica
        self.kategorije = kategorije

    def __str__(self):
        return self.naziv

kategorije = [
    Kategorija(oznaka="K1", naziv="Slatko"),
    Kategorija(oznaka="K2", naziv="Slano"),
    Kategorija(oznaka="K3", naziv="Cokolada"),
    Kategorija(oznaka="K4", naziv="Keks"),
    Kategorija(oznaka="K5", naziv="Mlecni proizvodi"),
    Kategorija(oznaka="K6", naziv="Voda"),
    Kategorija(oznaka="K7", naziv="Gazirano"),
    Kategorija(oznaka="K8", naziv="Negazirano"),
    Kategorija(oznaka="K9", naziv="Obuca"),
    Kategorija(oznaka="K10", naziv="Odeca"),
    Kategorija(oznaka="K11", naziv="Jakna"),
    Kategorija(oznaka="K12", naziv="Pantalone")
]

prodavnice = [
    Prodavnica(pib="2345", naziv="Market", adresa="Adresa 1", broj_telefona="0213333333"),
    Prodavnica(pib="1578", naziv="Megamarket", adresa="Adresa 2", broj_telefona="02355444"),
    Prodavnica(pib="3456", naziv="Krojac", adresa="Adresa 3", broj_telefona="01178321")
]

artikli = [
    Artikal(oznaka="P1", naziv="Mleko", opis="Mleko 1L", cena=30.2, na_akciji=True, prodavnica=prodavnice[1], kategorije=[kategorije[4]]),
    Artikal(oznaka="P2", naziv="Najlepse zelje cokolada", opis="200g", cena=70.0, na_akciji=False,prodavnica=prodavnice[1], kategorije=[kategorije[0], kategorije[2]]),
    Artikal(oznaka="P3", naziv="Pantalone", opis="Pamucne pantalone", cena=70.0, na_akciji=False, prodavnica=prodavnice[2], kategorije=[kategorije[9], kategorije[11]]),
    Artikal(oznaka="P4", naziv="Kaput", opis="Pamucni kaput", cena=7000.0, na_akciji=False, prodavnica=prodavnice[2], kategorije=[kategorije[9], kategorije[10]]),
]

podaci = {"kategorije": kategorije,"prodavnice": prodavnice, "artikli": artikli}
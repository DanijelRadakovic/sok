from django.core.management.base import BaseCommand

from ...models import Prodavnica,Kategorija,Artikal


class Command(BaseCommand):
    #args = '<args1 args2>'
    help = 'Komanda za popunjavanje baze sa inicijalnim vrednostima'

    def _ubaci_prodavnice(self):
        Prodavnica.objects.all().delete()

        p1=Prodavnica(pib="2345",naziv="Market",adresa="Adresa 1",broj_telefona="0213333333")
        p1.save()

        p2 = Prodavnica(pib="1578", naziv="Megamarket", adresa="Adresa 2", broj_telefona="02355444")
        p2.save()

        p3 = Prodavnica(pib="3456", naziv="Krojac", adresa="Adresa 3", broj_telefona="01178321")
        p3.save()

    def _ubaci_kategorije(self):
        Kategorija.objects.all().delete()

        k1 = Kategorija(oznaka="K1", naziv="Slatko")
        k1.save()

        k2 = Kategorija(oznaka="K2", naziv="Slano")
        k2.save()

        k3 = Kategorija(oznaka="K3", naziv="Cokolada")
        k3.save()

        k4 = Kategorija(oznaka="K4", naziv="Keks")
        k4.save()

        k5 = Kategorija(oznaka="K5", naziv="Mlecni proizvodi")
        k5.save()

        k6 = Kategorija(oznaka="K6", naziv="Voda")
        k6.save()

        k7 = Kategorija(oznaka="K7", naziv="Gazirano")
        k7.save()

        k8 = Kategorija(oznaka="K8", naziv="Negazirano")
        k8.save()

        k9 = Kategorija(oznaka="K9", naziv="Obuca")
        k9.save()

        k10 = Kategorija(oznaka="K10", naziv="Odeca")
        k10.save()

        k11 = Kategorija(oznaka="K11", naziv="Jakna")
        k11.save()

        k12 = Kategorija(oznaka="K12", naziv="Pantalone")
        k12.save()
    def _ubaci_artikle(self):
        Artikal.objects.all().delete()

        a1 = Artikal(oznaka="P1", naziv="Mleko", opis="Mleko 1L", cena=30.2, na_akciji=True)
        a1.prodavnica = Prodavnica.objects.get(pib="1578")

        a1.save()
        a1.kategorije.add(Kategorija.objects.get(oznaka="K5"))
        a1.save()

        a2 = Artikal(oznaka="P2", naziv="Najlepse zelje cokolada", opis="200g", cena=70.0, na_akciji=False)
        a2.prodavnica = Prodavnica.objects.get(pib="1578")

        a2.save()
        a2.kategorije.add(Kategorija.objects.get(oznaka="K3"))
        a2.kategorije.add(Kategorija.objects.get(oznaka="K1"))
        a2.save()

        a3 = Artikal(oznaka="P3", naziv="Pantalone", opis="Pamucne pantalone", cena=70.0, na_akciji=False)
        a3.prodavnica = Prodavnica.objects.get(pib="3456")

        a3.save()
        a3.kategorije.add(Kategorija.objects.get(oznaka="K10"))
        a3.kategorije.add(Kategorija.objects.get(oznaka="K12"))
        a3.save()

        a4 = Artikal(oznaka="P4", naziv="Kaput", opis="Pamucni kaput", cena=7000.0, na_akciji=False)
        a4.prodavnica = Prodavnica.objects.get(pib="3456")

        a4.save()
        a4.kategorije.add(Kategorija.objects.get(oznaka="K10"))
        a4.kategorije.add(Kategorija.objects.get(oznaka="K11"))
        a4.save()

    def handle(self, *args, **options):
        self._ubaci_prodavnice()
        self._ubaci_kategorije()
        self._ubaci_artikle()
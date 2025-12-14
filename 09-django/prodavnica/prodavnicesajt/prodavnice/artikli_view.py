from django.apps.registry import apps
from django.shortcuts import render, get_object_or_404, redirect

from .util import convert_to_float, convert_to_boolean
from .models import Artikal, Prodavnica, Kategorija


def lista_artikala(request):
    title=apps.get_app_config('prodavnice').verbose_name
    artikli=Artikal.objects.all()
    return render(request,"lista_artikala.html",{"title":title,"artikli":artikli})

def brisanje_artikla(request,id):
    a=get_object_or_404(Artikal,id=id)
    a.delete()
    return redirect('lista_artikala')


def unos_artikla(request,id=None):
    title=apps.get_app_config('prodavnice').verbose_name
    if request.method=='GET':
        prodavnice=Prodavnica.objects.all()
        greska_artikli=None
        if not prodavnice.exists():
            greska_artikli="Da biste mogli da unosite Artikle morate uneti bar jednu prodavnicu."
        lista_kategorija=Kategorija.objects.all()
        greska_lista_kategorije=None
        if not lista_kategorija.exists():
            greska_lista_kategorije="Da biste mogli da unosite Artikle morate uneti bar jednu kategoriju."

        if greska_artikli or greska_lista_kategorije:
            return render(request, "unos_artikla.html",
                          {"title": title, "greska_artikli":greska_artikli, "greska_lista_kategorije":greska_lista_kategorije})

        if id is None:
            return render(request,"unos_artikla.html",{"title":title,"prodavnice":prodavnice,"lista_kategorija":lista_kategorija})
        else:
            stari_id=id
            a=Artikal.objects.get(id=id)
            kategorije=a.kategorije.all()
            return render(request,"unos_artikla.html",{"title":title,"stari_id":stari_id,"oznaka":a.oznaka,
                               "naziv":a.naziv,"opis":a.opis,"cena":a.cena,"na_akciji":a.na_akciji,"kategorije":kategorije,
                               "prodavnica":a.prodavnica,"prodavnice":prodavnice,"lista_kategorija":lista_kategorija})
    else:
        greska_oznaka=None
        greska_naziv=None
        greska_opis=None
        greska_cena=None
        greska_na_akciji = None
        greska_kategorije = None
        greska_prodavnica = None
        oznaka = request.POST['oznaka']
        naziv = request.POST['naziv']
        opis = request.POST['opis']
        cena, cena_converted = convert_to_float(request.POST['cena'])
        try:
            na_akciji, na_akciji_converted = convert_to_boolean(request.POST['na_akciji'])
        except:
            na_akciji=False

        kategorije_lista =request.POST.getlist('kategorije')
        prodavnica = request.POST['prodavnica']


        try:
            stari_id = request.POST['stari_id']
        except:
            stari_id = None

        if oznaka is not None and oznaka == "":
            greska_oznaka="Morate uneti oznaku"
        if naziv is not None and naziv == "":
            greska_naziv="Morate uneti naziv"
        if opis is not None and opis == "":
            greska_opis="Morate uneti opis"
        if cena is not None and cena == "":
            greska_cena="Morate uneti cenu"

        if kategorije_lista is not None and kategorije_lista == "":
            greska_kategorije="Morate izabrati kategorije"
        if prodavnica is not None and prodavnica == "":
            greska_prodavnica="Morate izabrati prodavnicu"

        if not cena_converted:
            greska_cena="Morate uneti decimalnu vrednost za cenu"
        if greska_prodavnica is None:
            p=Prodavnica.objects.get(id=prodavnica)
            if p is not None:
                prodavnica=p
            else:
                greska_prodavnica="Izabrana prodavnica ne postoji"

        if greska_oznaka is None:
            try:
                a = Artikal.objects.get(oznaka=oznaka)
                if stari_id is not None:
                    a2 = Artikal.objects.get(id=stari_id)
                    if a2.oznaka != a.oznaka:
                        greska_oznaka = "Artikal sa tom vrednoscu oznake vec postoji"
                else:
                    greska_oznaka = "Artikal sa tom vrednoscu oznake vec postoji"
            except:
                pass


        kategorije=[]
        for k_oznaka in kategorije_lista:
            try:
                k=Kategorija.objects.get(id=k_oznaka)
                kategorije.append(k)
            except:
                pass
        if len(kategorije)==0:
            greska_kategorije="Morate izabrati kategoriju"

        if greska_oznaka is None and greska_naziv is None and greska_opis is None and greska_cena is None \
                and greska_na_akciji is None and greska_kategorije is None and greska_prodavnica is None:
            if stari_id is None:
                    a=Artikal(oznaka=oznaka,naziv=naziv,opis=opis,cena=cena,na_akciji=na_akciji)
                    a.prodavnica=prodavnica
                    a.save()
                    for k in kategorije:
                        a.kategorije.add(k)
                    a.save()
            else:
                a = Artikal.objects.get(id=stari_id)
                a.oznaka=oznaka
                a.naziv=naziv
                a.opis=opis
                a.cena=cena
                a.na_akciji=na_akciji
                for k in a.kategorije.all():
                    a.kategorije.remove(k)
                for k in kategorije:
                    a.kategorije.add(k)
                a.prodavnica=prodavnica
                a.save()
            return redirect('lista_artikala')
        prodavnice = Prodavnica.objects.all()
        lista_kategorija = Kategorija.objects.all()
        return render(request,"unos_artikla.html",{"title":title,"greska_oznaka":greska_oznaka,
                                   "greska_naziv":greska_naziv,"greska_opis":greska_opis,
                                   "greska_cena":greska_cena, "greska_na_akciji":greska_na_akciji,
                                   "greska_kategorije":greska_kategorije,"greska_prodavnica":greska_prodavnica,
                                   "oznaka":oznaka,"naziv":naziv,"opis":opis,"cena":cena,
                                   "na_akciji":na_akciji,"stari_id":stari_id,
                                   "kategorije":kategorije,"prodavnica":prodavnica,
                                   "prodavnice":prodavnice,"lista_kategorija":lista_kategorija}
                                   )

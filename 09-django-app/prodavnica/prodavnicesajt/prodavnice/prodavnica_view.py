from django.apps.registry import apps
from django.shortcuts import render, get_object_or_404, redirect

from .models import Prodavnica


def lista_prodavnica(request):
    title=apps.get_app_config('prodavnice').verbose_name
    prodavnice=Prodavnica.objects.all()
    return render(request,"lista_prodavnica.html",{"title":title,"prodavnice":prodavnice})

def brisanje_prodavnice(request,id):
    p=get_object_or_404(Prodavnica,id=id)
    p.delete()
    return redirect('lista_prodavnica')

def unos_prodavnice(request,id=None):
    title = apps.get_app_config('prodavnice').verbose_name
    if request.method=='GET':
        if id is None:
            return render(request,"unos_prodavnice.html",{"title":title})
        else:
            p = get_object_or_404(Prodavnica, id=id)
            stari_id=id
            return render(request,"unos_prodavnice.html",{"title":title,"stari_id":stari_id,"pib":p.pib,
                               "naziv":p.naziv,"adresa":p.adresa,"broj_telefona":p.broj_telefona})
    else:
        greska_pib=None
        greska_naziv=None
        greska_adresa=None
        greska_broj_telefona=None
        pib = request.POST['pib']
        naziv = request.POST['naziv']
        adresa = request.POST['adresa']
        broj_telefona= request.POST['broj_telefona']

        try:
            stari_id = request.POST['stari_id']
        except:
            stari_id = None

        if pib is not None and pib =="":
            greska_pib="Morate uneti pib"
        if naziv is not None and naziv == "":
            greska_naziv="Morate uneti naziv"
        if adresa is not None and adresa == "":
            greska_adresa="Morate uneti adresu"
        if broj_telefona is not None and broj_telefona == "":
            greska_broj_telefona = "Morate uneti broj telefona"

        if greska_pib is None:
            try:
                p = Prodavnica.objects.get(pib=pib)
                if stari_id is not None:
                    p2 = Prodavnica.objects.get(id=stari_id)
                    if p2.pib != p.pib:
                        greska_pib = "Prodavnica sa tom vrednoscu pib-a vec postoji"
                else:
                    greska_pib = "Prodavnica sa tom vrednoscu pib-a vec postoji"
            except:
                pass

        if greska_pib is None and greska_adresa is None and greska_naziv is None and greska_broj_telefona is None:
            if stari_id is None:
                p=Prodavnica(pib=pib,naziv=naziv,adresa=adresa,broj_telefona=broj_telefona)
                p.save()
            else:
                p = Prodavnica.objects.get(id=stari_id)
                p.pib=pib
                p.naziv=naziv
                p.adresa=adresa
                p.broj_telefona=broj_telefona
                p.save()
            return redirect('lista_prodavnica')
        return render(request,"unos_prodavnice.html",{"title":title,"greska_pib":greska_pib,
                                   "greska_naziv":greska_naziv,"greska_adresa":greska_adresa,
                                   "greska_broj_telefona":greska_broj_telefona,
                                   "pib":pib,"naziv":naziv,"adresa":adresa,
                                   "broj_telefona":broj_telefona,"stari_id":stari_id}
                                   )

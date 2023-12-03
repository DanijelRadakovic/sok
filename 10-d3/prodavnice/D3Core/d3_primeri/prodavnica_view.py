from d3_primeri.models import Prodavnica, Artikal
from django.apps.registry import apps
from django.shortcuts import render


def foce_layout(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    prodavnice=Prodavnica.objects.all()
    artikli=Artikal.objects.all()
    return render(request,"primerProdavnicaForceLayout.html",
                  {"title":"Primer prodavnica force layout",
                   "plugini_ucitavanje": plugini,
                   "prodavnice":prodavnice,
                   "artikli":artikli})

def tree_layout(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    prodavnice=Prodavnica.objects.all()
    artikli=Artikal.objects.all()
    return render(request,"primerProdavnicaTreeLayout.html",
                  {"title":"Primer prodavnica force layout",
                   "plugini_ucitavanje": plugini,
                   "prodavnice":prodavnice,
                   "artikli":artikli})
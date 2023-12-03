from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "index.html", {"title": "Index", "plugini_ucitavanje": plugini})


def ucitavanje_plugin(request, id):
    # Cuvanje identifikatora plugina na nivou sesije.
    request.session['izabran_plugin_ucitavanje'] = id
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    # Trazimo plugin sa prosledjenim identifikatorom,
    for i in plugini:
        if i.identifier() == id:
            # te pozivamo funkciju koja podatke upisuje u bazu.
            i.ucitati()
    return redirect('index')


def primer1(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer1.html", {"title": "Primer1", "plugini_ucitavanje": plugini})


def primer2(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer2.html", {"title": "Primer2", "plugini_ucitavanje": plugini})


def primer3(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer3.html", {"title": "Primer3", "plugini_ucitavanje": plugini})


def primer4(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primer4.html", {"title": "Primer4", "plugini_ucitavanje": plugini})


def primerPanZoom(request):
    plugini = apps.get_app_config('d3_primeri').plugini_ucitavanje
    return render(request, "primerPanZoom.html", {"title": "Primer Pan Zoom", "plugini_ucitavanje": plugini})

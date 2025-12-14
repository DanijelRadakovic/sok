from django.apps.registry import apps
from django.shortcuts import render

from .models import Kategorija


def index(request):
    title = apps.get_app_config('prodavnice').verbose_name
    return render(request,'index.html',{"title":title})

def lista_kategorija(request):
    kategorije=Kategorija.objects.all()
    title=apps.get_app_config('prodavnice').verbose_name
    return render(request,"lista_kategorija.html",{"title":title,"kategorije":kategorije})


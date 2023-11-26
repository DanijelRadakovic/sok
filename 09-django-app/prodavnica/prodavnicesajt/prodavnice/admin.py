from django.contrib import admin

from .models import Prodavnica, Kategorija, Artikal

admin.site.register(Prodavnica)
admin.site.register(Kategorija)
admin.site.register(Artikal)

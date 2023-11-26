from django.urls import path

from . import views,artikli_view,prodavnica_view

urlpatterns = [
    path('', views.index, name='index'),
    path('kategorije/', views.lista_kategorija, name='lista_kategorija'),
    path('artikli/', artikli_view.lista_artikala, name='lista_artikala'),
    path('brisanje/artikla/<int:id>', artikli_view.brisanje_artikla, name='brisanje_artikla'),
    path('unos/artikla/', artikli_view.unos_artikla, name='unos_artikla'),
    path('unos/artikla/<int:id>', artikli_view.unos_artikla, name='unos_artikla_p'),
    path('prodavnice/', prodavnica_view.lista_prodavnica, name='lista_prodavnica'),
    path('brisanje/prodavnice/<int:id>', prodavnica_view.brisanje_prodavnice, name='brisanje_prodavnice'),
    path('unos/prodavnice/', prodavnica_view.unos_prodavnice, name='unos_prodavnice'),
    path('unos/prodavnice/<int:id>', prodavnica_view.unos_prodavnice, name='unos_prodavnice_p'),
]
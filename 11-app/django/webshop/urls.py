from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('plugin/datasource/<str:id>', views.datasource_plugin, name="datasource_plugin"),
    path('layout/tree', views.tree_layout, name="tree_layout"),
]
from django.apps import apps
from django.shortcuts import render, redirect
from shop.use_cases.plugin_recognition import PluginService

from shop.use_cases.shop_tree_view import TreeView
from .apps import datasource_group


def index(request):
    plugin_service: PluginService = apps.get_app_config('webshop').plugin_service
    datasource_plugins = plugin_service.plugins[datasource_group]
    return render(request, 'index.html', {'title': 'Index', 'datasource_plugins': datasource_plugins})


def datasource_plugin(request, id):
    request.session['selected_datasource_plugin'] = id
    return redirect('index')


def tree_layout(request):
    selected_plugin = request.session['selected_datasource_plugin']
    plugin_service: PluginService = apps.get_app_config('webshop').plugin_service
    datasource_plugins = plugin_service.plugins[datasource_group]

    tree_view = TreeView(plugin_service)
    header, body = tree_view.render(selected_plugin)


    return render(request, 'shop-tree-layout.html',
                  {'title': 'Shop tree layout',
                   'datasource_plugins': datasource_plugins,
                   'tree_view_header': header,
                   'tree_view_body': body})
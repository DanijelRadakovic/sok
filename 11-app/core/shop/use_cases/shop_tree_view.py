import os
import sys
from jinja2 import Template
from typing import List

from shop.api.model import Shop

from .const import DATASOURCE_GROUP
from .plugin_recognition import PluginService

class TreeView(object):

    def __init__(self, plugin_service: PluginService):
        self.__plugin_service = plugin_service

    def render(self, plugin_id: str, **kwargs) -> (str, str):
        """
        Returns the required header and body html content that needs to be included in page
        in order to provide tree view layout.
        :param plugin_id: ID of the datasource plugin that is used for fetchin data.
        :param kwargs: Arguments for the datasource plugin.
        :return: (header,body) html string that should be included in page.
        """
        shops = []
        plugins = self.__plugin_service.plugins[DATASOURCE_GROUP]
        for p in plugins:
            if p.identifier() == plugin_id:
                shops = p.load(**kwargs)

        tree_data  = self.__generate_tree_data(shops)
        import json
        data_json = json.dumps(tree_data, ensure_ascii=False)

        with open(os.path.join(sys.prefix, 'templates/shop-tree-layout-header.html'), 'r', encoding='utf-8') as file:
            header_html = file.read()

        with open(os.path.join(sys.prefix, 'templates/shop-tree-layout-body.html'), 'r', encoding='utf-8') as file:
            body_template = file.read()

        body_html = Template(body_template).render(data_json=data_json)
        return header_html, body_html

    def __generate_tree_data(self, shops: List[Shop]):
        children = []
        for s in shops:
            shop = {
                'id': f'shop_{s.pib}',
                'name': s.name,
                'children': [
                    {
                        'id': f'article_{a.code}',
                        'name': a.name,
                        'children': [
                            {
                                'id': f'category_{c.code}',
                                'name': c.name,
                                'size': '20'
                            } for c in a.categories
                        ]
                    }
                    for a in s.articles
                ]
            }

            children.append(shop)

        data = {
            'id': 'Shops',
            "name": 'Shops',
            'children': children
        }

        return data

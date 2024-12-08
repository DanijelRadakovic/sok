from typing import List

from shop.api.model import Shop
from shop.api.services.plugin import DataSourcePlugin

from shop.api.model import Category, Article


class CodeDatasource(DataSourcePlugin):
    def name(self) -> str:
        return "Shop Code Datasource"

    def identifier(self) -> str:
        return "datasource_code"

    def load(self) -> List[Shop]:
        c1 = Category(code='C1', name='sport')
        c2 = Category(code='C2', name='sedan')

        s1 = Shop(pib='1234', name='JDM dealers', address='somewhere in Japan', phone='1234')
        a1 = Article(code='N1', name='Nissan GTR', description='supercar', on_sale=False, price=150, categories=[c1])
        a2 = Article(code='S1', name='Subaru WRX', description='sportcar', on_sale=True, price=100, categories=[c1])
        s1.add_articles([a1, a2])

        s2 = Shop(pib='5679', name='German dealers', address='somewhere in Germany', phone='5678')
        a3 = Article(code='RS5', name='Audi RS5', description='sportcar', on_sale=False, price=70, categories=[c2])
        a4 = Article(code='RS6', name='Audi RS6', description='sportcar', on_sale=True, price=90, categories=[c2])
        s2.add_articles([a3, a4])

        return [s1, s2]

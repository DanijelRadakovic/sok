from typing import List

from shop.api.model import Shop
from shop.api.services.plugin import DataSourcePlugin
from .model import Shop as ShopDao
from .init_data import insert_shops, insert_articles, insert_categories
from .mappers import convert_shop_dao_into_entity


class DatabaseDatasource(DataSourcePlugin):
    def name(self) -> str:
        return "Shop Database Datasource"

    def identifier(self) -> str:
        return "datasource_db"

    def load(self) -> List[Shop]:
        insert_categories()
        insert_shops()
        insert_articles()
        shops = ShopDao.objects.all()
        return [convert_shop_dao_into_entity(shop) for shop in shops]

from typing import List

from shop.api.model import Shop
from shop.api.services.plugin import DataSourcePlugin
from .manager import DatabaseManager
from .init_data import insert_shops,insert_articles,insert_categories
from .mappers import convert_shop_dao_into_entity


class DatabaseDatasource(DataSourcePlugin):
    def name(self) -> str:
        return "Shop Database Datasource"

    def identifier(self) -> str:
        return "datasource_db"

    def load(self) -> List[Shop]:
        db = DatabaseManager("shop.db")
        insert_categories(db)
        insert_shops(db)
        insert_articles(db)
        shops = db.get_all_shops()
        shops = [convert_shop_dao_into_entity(db,shop) for shop in shops]
        db.close()
        return shops

import unittest

from .manager import DatabaseManager
from .init_data import insert_shops,insert_articles,insert_categories
from .datasource import DatabaseDatasource

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseManager(":memory:")

    def tearDown(self):
        self.db.close()

    def test_init_data(self):
        insert_categories(self.db)
        insert_shops(self.db)
        insert_articles(self.db)
        shops = self.db.get_all_shops()

        self.assertEqual(len(shops), 3)

    def test_database_datasource(self):
        plugin = DatabaseDatasource()
        shops = plugin.load()
        self.assertEqual(len(shops), 3)

if __name__ == '__main__':
    unittest.main()
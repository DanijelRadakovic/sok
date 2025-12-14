import sqlite3
from typing import List
from .model import *


class DatabaseManager:
    def __init__(self, db_name="inventory.db"):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS shop (id INTEGER PRIMARY KEY, pib TEXT, name TEXT, address TEXT, phone TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY, code TEXT, name TEXT)")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS article (id INTEGER PRIMARY KEY, code TEXT, name TEXT, description TEXT, price REAL, on_sale INTEGER, shop_id INTEGER, FOREIGN KEY(shop_id) REFERENCES shop(id))")
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS article_category_map (article_id INTEGER, category_id INTEGER, FOREIGN KEY(article_id) REFERENCES article(id), FOREIGN KEY(category_id) REFERENCES category(id))")
        self.conn.commit()

    def clear_table(self, table_name):
        self.cursor.execute(f"DELETE FROM {table_name}")
        self.conn.commit()

    def get_shop_id_by_pib(self, pib) -> int:
        self.cursor.execute("SELECT id FROM shop WHERE pib = ?", (pib,))
        result = self.cursor.fetchone()
        if result:
            return result['id']
        raise ValueError(f"Shop with pib {pib} not found")

    def get_category_id_by_code(self, code) -> int:
        self.cursor.execute("SELECT id FROM category WHERE code = ?", (code,))
        result = self.cursor.fetchone()
        if result:
            return result['id']
        raise ValueError(f"Category with code {code} not found")

    def save_shop(self, shop: Shop):
        self.cursor.execute("INSERT INTO shop (pib, name, address, phone) VALUES (?, ?, ?, ?)",
                            (shop.pib, shop.name, shop.address, shop.phone))
        self.conn.commit()

    def save_category(self, cat: Category):
        self.cursor.execute("INSERT INTO category (code, name) VALUES (?, ?)",
                            (cat.code, cat.name))
        self.conn.commit()

    def save_article(self, article: Article, category_ids: List[int]):
        self.cursor.execute("""
            INSERT INTO article (code, name, description, price, on_sale, shop_id) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            article.code, article.name, article.description, article.price, 1 if article.on_sale else 0,
            article.shop_id))

        new_article_id = self.cursor.lastrowid

        for cat_id in category_ids:
            self.cursor.execute("INSERT INTO article_category_map (article_id, category_id) VALUES (?, ?)",
                                (new_article_id, cat_id))
        self.conn.commit()

    def get_all_shops(self) -> List[Shop]:
        self.cursor.execute("SELECT * FROM shop")
        rows = self.cursor.fetchall()

        return [
            Shop(
                id=row['id'],
                pib=row['pib'],
                name=row['name'],
                address=row['address'],
                phone=row['phone']
            ) for row in rows
        ]

    def get_articles_by_shop_id(self, shop_id: int) -> List[Article]:
        self.cursor.execute("SELECT * FROM article WHERE shop_id = ?", (shop_id,))
        rows = self.cursor.fetchall()

        return [
            Article(
                id=row['id'],
                code=row['code'],
                name=row['name'],
                description=row['description'],
                price=row['price'],
                on_sale=bool(row['on_sale']),
                shop_id=row['shop_id']
            ) for row in rows
        ]

    def get_categories_by_article_id(self, article_id: int) -> List[Category]:
        sql = """
            SELECT c.* 
            FROM category c
            JOIN article_category_map m ON c.id = m.category_id
            WHERE m.article_id = ?
        """
        self.cursor.execute(sql, (article_id,))
        rows = self.cursor.fetchall()

        return [
            Category(
                id=row['id'],
                code=row['code'],
                name=row['name']
            ) for row in rows
        ]

    def close(self):
        self.conn.close()

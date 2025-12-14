from .manager import DatabaseManager
from .model import *


def insert_shops(db: DatabaseManager):
    print("Inserting Shops...")
    db.clear_table('shop')

    s1 = Shop(id=None, pib="2345", name="Market", address="Adresa 1", phone="0213333333")
    db.save_shop(s1)

    s2 = Shop(id=None, pib="1578", name="Megamarket", address="Adresa 2", phone="02355444")
    db.save_shop(s2)

    s3 = Shop(id=None, pib="3456", name="Krojac", address="Adresa 3", phone="01178321")
    db.save_shop(s3)


def insert_categories(db: DatabaseManager):
    print("Inserting Categories...")
    db.clear_table('category')

    categories_data = [
        ("K1", "Slatko"),
        ("K2", "Slano"),
        ("K3", "Cokolada"),
        ("K4", "Keks"),
        ("K5", "Mlecni proizvodi"),
        ("K6", "Voda"),
        ("K7", "Gazirano"),
        ("K8", "Negazirano"),
        ("K9", "Obuca"),
        ("K10", "Odeca"),
        ("K11", "Jakna"),
        ("K12", "Pantalone")
    ]

    for code, name in categories_data:
        c = Category(id=None, code=code, name=name)
        db.save_category(c)


def insert_articles(db: DatabaseManager):
    print("Inserting Articles...")
    db.clear_table('article')
    db.clear_table('article_category_map')

    shop_id_1 = db.get_shop_id_by_pib("1578")
    a1 = Article(id=None, code="P1", name="Mleko", description="Mleko 1L", price=30.2, on_sale=True, shop_id=shop_id_1)
    cat_ids_1 = [
        db.get_category_id_by_code("K5")
    ]
    db.save_article(a1, cat_ids_1)

    shop_id_2 = db.get_shop_id_by_pib("1578")
    a2 = Article(id=None, code="P2", name="Najlepse zelje cokolada", description="200g", price=70.0, on_sale=False,
                 shop_id=shop_id_2)
    cat_ids_2 = [
        db.get_category_id_by_code("K3"),
        db.get_category_id_by_code("K1")
    ]
    db.save_article(a2, cat_ids_2)

    shop_id_3 = db.get_shop_id_by_pib("3456")
    a3 = Article(id=None, code="P3", name="Pantalone", description="Pamucne pantalone", price=70.0, on_sale=False,
                 shop_id=shop_id_3)
    cat_ids_3 = [
        db.get_category_id_by_code("K10"),
        db.get_category_id_by_code("K12")
    ]
    db.save_article(a3, cat_ids_3)

    shop_id_4 = db.get_shop_id_by_pib("3456")
    a4 = Article(id=None, code="P4", name="Kaput", description="Pamucni kaput", price=7000.0, on_sale=False,
                 shop_id=shop_id_4)
    cat_ids_4 = [
        db.get_category_id_by_code("K10"),
        db.get_category_id_by_code("K11")
    ]
    db.save_article(a4, cat_ids_4)

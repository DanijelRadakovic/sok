from shop.api.model import Shop, Article, Category
from .model import Shop as ShopDao, Article as ArticleDao, Category as CategoryDao

def convert_shop_dao_into_entity(db, shop_dao: ShopDao) -> Shop:
    s = Shop(pib=shop_dao.pib, name=shop_dao.name, address=shop_dao.address, phone=shop_dao.phone)
    article_daos = db.get_articles_by_shop_id(shop_dao.id)
    converted_articles = [convert_article_dao_to_entity(db, a) for a in article_daos]
    s.add_articles(converted_articles)
    return s


def convert_article_dao_to_entity(db, article_dao: ArticleDao) -> Article:
    category_daos = db.get_categories_by_article_id(article_dao.id)
    categories = [convert_category_dao_to_entity(c) for c in category_daos]
    return Article(
        code=article_dao.code,
        name=article_dao.name,
        description=article_dao.description,
        price=float(article_dao.price),
        on_sale=article_dao.on_sale,
        categories=categories,
    )


def convert_category_dao_to_entity(category_dao: CategoryDao) -> Category:
    return Category(code=category_dao.code, name=category_dao.name)
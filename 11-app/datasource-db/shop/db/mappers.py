from .model import Shop as ShopDao, Article as ArticleDao, Category as CategoryDao
from shop.api.model import Shop, Article, Category

def convert_shop_dao_into_entity(shop: ShopDao) -> Shop:
    s = Shop(pib=shop.pib, name=shop.name, address=shop.address, phone=shop.phone)
    articles = ArticleDao.objects.filter(shop=shop)
    s.add_articles([convert_article_dao_to_entity(a) for a in articles])
    return s

def convert_article_dao_to_entity(article: ArticleDao) -> Article:
    categories = [convert_category_dao_to_entity(c) for c in article.category.all()]
    return Article(
        code=article.code,
        name=article.name,
        description=article.description,
        price=float(article.price),
        on_sale=article.on_sale,
        categories=categories,
    )

def convert_category_dao_to_entity(category: CategoryDao) -> Category:
    return Category(code=category.code, name=category.name)
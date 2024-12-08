from .model import Shop, Article, Category

def insert_shops():
    Shop.objects.all().delete()

    Shop(pib="2345", name="Market", address="Adresa 1", phone="0213333333").save()
    Shop(pib="1578", name="Megamarket", address="Adresa 2", phone="02355444").save()
    Shop(pib="3456", name="Krojac", address="Adresa 3", phone="01178321").save()


def insert_categories():
    Category.objects.all().delete()

    Category(code="K1", name="Slatko").save()
    Category(code="K2", name="Slano").save()
    Category(code="K3", name="Cokolada").save()
    Category(code="K4", name="Keks").save()
    Category(code="K5", name="Mlecni proizvodi").save()
    Category(code="K6", name="Voda").save()
    Category(code="K7", name="Gazirano").save()
    Category(code="K8", name="Negazirano").save()
    Category(code="K9", name="Obuca").save()
    Category(code="K10", name="Odeca").save()
    Category(code="K11", name="Jakna").save()
    Category(code="K12", name="Pantalone").save()


def insert_articles():
    Article.objects.all().delete()

    a1 = Article(code="P1", name="Mleko", description="Mleko 1L", price=30.2, on_sale=True)
    a1.shop = Shop.objects.get(pib="1578")

    a1.save()
    a1.category.add(Category.objects.get(code="K5"))
    a1.save()

    a2 = Article(code="P2", name="Najlepse zelje cokolada", description="200g", price=70.0, on_sale=False)
    a2.shop = Shop.objects.get(pib="1578")

    a2.save()
    a2.category.add(Category.objects.get(code="K3"))
    a2.category.add(Category.objects.get(code="K1"))
    a2.save()

    a3 = Article(code="P3", name="Pantalone", description="Pamucne pantalone", price=70.0, on_sale=False)
    a3.shop = Shop.objects.get(pib="3456")

    a3.save()
    a3.category.add(Category.objects.get(code="K10"))
    a3.category.add(Category.objects.get(code="K12"))
    a3.save()

    a4 = Article(code="P4", name="Kaput", description="Pamucni kaput", price=7000.0, on_sale=False)
    a4.shop = Shop.objects.get(pib="3456")

    a4.save()
    a4.category.add(Category.objects.get(code="K10"))
    a4.category.add(Category.objects.get(code="K11"))
    a4.save()

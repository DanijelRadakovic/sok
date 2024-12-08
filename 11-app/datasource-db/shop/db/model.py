from django.db import models

class Shop(models.Model):
    pib=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=40)
    phone=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    code=models.CharField(max_length=20)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    code=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    on_sale=models.BooleanField('on sale')
    category=models.ManyToManyField(Category)
    shop=models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name

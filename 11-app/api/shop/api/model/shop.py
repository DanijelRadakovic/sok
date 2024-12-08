from typing import List
from .article import Article

class Shop(object):
    def __init__(self, pib: str, name: str, address: str, phone: str):
        self.__pib = pib
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__articles: List[Article] = []

    @property
    def pib(self):
        return self.__pib

    @pib.setter
    def pib(self, value: str):
        if isinstance(value, str):
            self.__pib = value
        else:
            raise TypeError('Value must be type of str')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str):
            self.__name = value
        else:
            raise TypeError('Value must be type of str')

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        if isinstance(value, str):
            self.__address = value
        else:
            raise TypeError('Value must be type of str')

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if isinstance(value, str):
            self.__phone = value
        else:
            raise TypeError('Value must be type of str')

    @property
    def articles(self):
        return self.__articles

    def add_article(self, article: Article):
        self.__articles.append(article)

    def add_articles(self, articles: List[Article]):
        self.__articles += articles

    def __str__(self):
        return self.name
from typing import List
from .category import Category


class Article(object):
    def __init__(self,
                 code: str,
                 name: str,
                 description: str,
                 price: float,
                 on_sale: bool,
                 categories: List[Category]):
        self.__code = code
        self.__name = name
        self.__description = description
        self.__price = price
        self.__on_sale = on_sale
        self.__categories = categories

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        if isinstance(value, str):
            self.__code = value
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
    def description(self):
        return self.__description

    @description.setter
    def description(self, value: str):
        if isinstance(value, str):
            self.__description = value
        else:
            raise TypeError('Value must be type of str')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if isinstance(value, float):
            self.__price = value
        else:
            raise TypeError('Value must be type of float')

    @property
    def on_sale(self):
        return self.__on_sale

    @on_sale.setter
    def on_sale(self, value: bool):
        if isinstance(value, bool):
            self.__on_sale = value
        else:
            raise TypeError('Value must be type of bool')

    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, value: List[Category]):
        self.__categories = value

    def __str__(self):
        return self.name

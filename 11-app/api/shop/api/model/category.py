class Category(object):
    def __init__(self, code: str, name: str):
        self.__code = code
        self.__name = name

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

    def __str__(self):
        return self.name

class Foo(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value

    @name.deleter
    def name(self):
        raise TypeError("Can't delete name")


if __name__ == '__main__':
    f = Foo("Guido")
    print(dir(f))
    n = f.name
    print("n:{}".format(n))
    f.name = "Monty"
    print("f.name:{}".format(f.name))
    try:
        f.name = 45
    except TypeError as e:
        print("Pogresan tip:{}".format(e))

    try:
        del f.name
    except Exception as e:
        print("Brisanje:{}".format(e))


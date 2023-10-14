class A(object):
    def __init__(self):
        self.__X = 3  # Izmenjeno u self._A__X

    def __spam(self):  # Izmenjeno u _A__spam()
        pass

    def skriveni_X_od_A(self):
        return self.__X

    def bar(self):
        self.__spam()  # Poziva A.__spam()

    def _foo(self):
        pass


class B(A):
    def __init__(self):
        super().__init__()
        self.__X = 37  # Izmenjeno u self._B__X

    def skriveni_X_od_B(self):
        return self.__X

    def __spam(self):  # Izmenjeno u _B__spam()
        pass


class C(object):
    pass


if __name__ == '__main__':
    a = A()
    print("dir(a):{}".format(dir(a)))
    print("a.skriveni_X_od_A():{}".format(a.skriveni_X_od_A()))
    print("a._A__X:{}".format(a._A__X))

    b = B()
    b._foo()
    print("dir(b):{}".format(dir(b)))
    print("b.skriveni_X_od_A():{}".format(b.skriveni_X_od_A()))
    print("b.skriveni_X_od_B():{}".format(b.skriveni_X_od_B()))
    print("b._A__X:{}".format(b._A__X))
    print("b._B__X:{}".format(b._B__X))

    c = C()
    print("type(a):{}".format(type(a)))  # Vraća klasu A (class objekat)

    print("isinstance(a, A):{}".format(isinstance(a, A)))  # True
    print("isinstance(b, A):{}".format(isinstance(b, A)))  # True, B nasleđuje A
    print("isinstance(b, C):{}".format(isinstance(b, C)))  # False, B ne nasleđuje C

    print("issubclass(B,A):{}".format(issubclass(B, A)))  # True
    print("issubclass(C,A):{}".format(issubclass(C, A)))  # False

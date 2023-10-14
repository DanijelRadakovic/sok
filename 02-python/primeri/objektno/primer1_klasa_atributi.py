class Klasa1(object):
    atribut = 0

    def __init__(self, parm1, parm2=20, parm3=30, *args, **kwargs):
        self.at1 = parm1
        self.at2 = parm2
        self.at3 = parm3
        try:
            self.at4 = args[0]
        except:
            self.at4 = "Parametar4"
        try:
            self.at5 = args[1]
        except:
            self.at5 = "Parametar5"
        self.at6 = kwargs.get("parm6", "Parametar6")
        self.at7 = kwargs.get("parm7", "Parametar7")

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.at1, self.at2, self.at3,
                                             self.at4, self.at5, self.at6,
                                             self.at7, )


if __name__ == '__main__':
    Klasa1.atribut = 10
    a = Klasa1(1)
    b = Klasa1(1, 2)
    c = Klasa1(1, parm3=3)
    d = Klasa1(1, 2, 3, 4, 5, 6, 7, parm4=40, parm5=50, parm6=60, parm7=70)

    print("A:" + str(a))
    print(a)
    print("B:{}".format(b))
    print("C:{}".format(c))
    print("D:{}".format(d))
    print("Deljeni atribut:{}".format(a.atribut))

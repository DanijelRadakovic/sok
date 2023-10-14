class Klasa(object):
    def __add__(self, other):
        print("Redefinisano sabiranje")

    def __sub__(self, other):
        print("Redefinisano oduzimanje")

    def __mul__(self, other):
        print("Redefinisano mnozenje")

    def __truediv__(self, other):
        print("Redefinisano deljenje")

    def __floordiv__(self, other):
        print("Redefinisano celobrojno deljenje")

    def __mod__(self, other):
        print("Redefinisano deljenje sa ostatkom")

    def __pow__(self, power, modulo=None):
        print("Redefinsano operator **")

    def __iadd__(self, other):
        print("Redefinisan operator +=")
        return self

    def __isub__(self, other):
        print("Redefinisan operator -=")
        return self

    def __imul__(self, other):
        print("Redefinisan operator *=")
        return self

    def __itruediv__(self, other):
        print("Redefinisan operator /=")
        return self

    def __ifloordiv__(self, other):
        print("Redefinisan operator //=")
        return self

    def __imod__(self, other):
        print("Redefinisan operator %=")
        return self

    def __ipow__(self, other):
        print("Redefinisan operator **=")
        return self

    def __eq__(self, other):
        print("Redefinisano poredjenje ==")

    def __le__(self, other):
        print("Redefinisano poredjenje <=")

    def __ge__(self, other):
        print("Redefinisano poredjenje >=")

    def __lt__(self, other):
        print("Redefinisano poredjenje <")

    def __gt__(self, other):
        print("Redefinisano poredjenje >")

    def __ne__(self, other):
        print("Redefinisan operator !=")

    def __del__(self):
        print("Redefinisan operator brisanje")

    def __len__(self):
        print("Redefinisano vracanje duzine vrednosti")
        return 0

    def __str__(self):
        print("Redefinisana metoda za string ispis")
        return ""

    def __repr__(self):
        print("Redefinisano vracanje string reprezentacije")
        return ""


if __name__ == '__main__':
    k1 = Klasa()

    k1 + 1
    k1 - 2
    k1 * 3
    k1 / 2

    k1 // 2
    k1 % 2

    k1 ** 3

    k1 += 1
    k1 -= 2
    k1 *= 3
    k1 /= 2

    k1 //= 2
    k1 %= 2
    k1 **= 3

    k1 == 3
    k1 <= 2
    k1 >= 4
    k1 < 4
    k1 > 5
    k1 != 7

    len(k1)

    str(k1)
    repr(k1)

    del k1

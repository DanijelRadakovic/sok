print("Ime modula primer1.py: ", __name__)
import sys

print("Ovo je sys.path:", sys.path)
import primer2


def osnovni_tipovi():
    a = 2
    b = 3.4
    c = True
    d = "Tekst"

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

    print(2 + 3)
    print(str(2) + " " + str(3))
    print("{:<5}|{:>07}|{:8.2}".format(a, c, b))


def relacioni_operatori():
    a = 10
    b = 20
    print(a > b)
    print(a < b)
    print(a <= b)
    print(a >= b)
    print(a != b)
    print(a == b)


def logicki_operatori():
    a = True
    b = False

    print(a and b)
    print(a or b)
    print(not a)


def poredjenje():
    a = 256
    b = 255 + 1
    print("Poredjenje po referenci")
    print(a is b)
    print(id(a), id(b))

    print("Poredjenje po vrednosti")
    print(a == b)

    c = 257
    d = 256 + 1

    print("Poredjenje po referenci")
    print(c is d)
    print(id(c), id(d))

    print("Poredjenje po vrednosti")
    print(c == d)


if __name__ == '__main__':
    print("Osnovni tipovi")
    osnovni_tipovi()

    print("\n", "Relacioni operatori", sep="")
    relacioni_operatori()

    print("\n", "Logicki operatori", sep="")
    logicki_operatori()

    print("\n", "Poredjenje", sep="")
    poredjenje()

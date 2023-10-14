def funkcija1(parm1, parm2):
    print(parm1, parm2)


def funkcija2(parm1, parm2=20, parm3="Tekst"):
    print(parm1, parm2, parm3)


def funkcija3(arg1, arg2=10, *args, **kwargs):
    print(arg1, arg2, type(args), args, type(kwargs), kwargs)

def funckija4(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


if __name__ == '__main__':
    funkcija1(10, 20)

    funkcija2(10)

    funkcija2(40, parm3="Novi tekst")

    # Nije validno, jer se imenovani argumenti/parametri mogu naci samo
    # posle neimenovanih
    # funkcija3(10, arg2=20, 30, 40, other=50)
    funkcija3(10, 20, 30, 40, other=50)

    list_args = [1, 2, 3]
    # raspakivanje argumenata iz liste
    funckija4(*list_args)
    tuple_args = tuple(list_args)
    # raspakivanje argumenata iz torke
    funckija4(*tuple_args)

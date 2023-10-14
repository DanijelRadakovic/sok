if __name__ == '__main__':
    names = ["Dave", "Mark", "Ann", "Phil"]
    print(names)

    a = names[2]  # Vraća treći objekat iz liste - "Ann"
    print(a)

    names[0] = "Jeff"  # Menja prvi objekat-referencu na "Jeff"
    names.append("Paula")  # Dodaje "Paula" na kraj liste
    print(names)
    names.insert(2, "Thomas")  # Ubacuje "Thomas" na lokaciju 2
    print(names)

    b = names[0:2]  # Vraća [ "Jeff", "Mark" ]
    c = names[2:]  # Vraća [ "Thomas", "Ann", "Phil", "Paula" ]
    print(b)
    print(c)

    names[1] = 'Jeff'  # Menja drugi element sa 'Jeff'
    names[0:2] = ['Dave', 'Mark', 'Jeff']  # Menja prva dva elementa sa liste
    # sa listom na desnoj strani
    a = [1, 2, 3] + [4, 5]  # Rezultat je [1,2,3,4,5]
    print(a)
    names = []  # Prazna lista
    names = list()  # Prazna lista

    a = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
    print(a[1])  # "Dave"
    print(a[3][2])  # 9
    print(a[3][3][1])  # 101

    for el in a:
        print(el,end="#")

    print()
    for i,el in enumerate(a):
        print("Redni broj:{} Element:{}".format(i,el))
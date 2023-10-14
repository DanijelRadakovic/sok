if __name__ == '__main__':
    s = set([3, 5, 9, 10])  # Kreira skup brojeva
    print(s)
    t = set("Hello") # Kreira skup jedinstvenih karaktera
    print(t)

    t.add('x')  # Dodavanje jednog elementa u t
    print(t)
    s.update([10, 37, 42])  # Dodavanje više elemenata u s
    print(s)
    t.remove('H')  # Uklanjanje elementa
    print(t)
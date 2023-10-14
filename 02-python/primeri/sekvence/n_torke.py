if __name__ == '__main__':
    stock = ('GOOG', 100, 490.10)
    print(stock)
    address = ('www.python.org', 80)
    print(address)
    first_name="Petar"
    last_name="Petrovic"
    phone="021222222"
    person = (first_name, last_name, phone)
    print(person)
    # ili samo
    stock = 'GOOG', 100, 490.10
    print(stock)
    address = 'www.python.org', 80
    print(address)
    person = first_name, last_name, phone
    print(person)
    item="Element"
    # Načini navođenja
    a = ()  # 0-tuple (prazan tuple)
    b = (item,)  # 1-tuple (obratiti pažnju na zarez)
    c = item,  # 1-tuple (obratiti pažnju na zarez)
    # "raspakivanje"
    name, shares, price = stock

    host, port = address

    first_name, last_name, phone = person

    people=[]
    people.append(person)
    first_name = "Jovan"
    last_name = "Jovanovic"
    phone = "021222222"
    person = (first_name, last_name, phone)
    people.append(person)

    print("Prikaz ljudi")
    for first_name,last_name,phone in people:
        print(first_name,last_name,phone)

    for i,el in enumerate(people):
        print("Redni broj:{} Element:{}".format(i,el))


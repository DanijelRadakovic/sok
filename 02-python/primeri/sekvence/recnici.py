if __name__ == '__main__':
    # Dva načina kreiranja praznog rečnika
    stock = {}
    stock = dict()
    # Kreiranje rečnika sa podacima
    stock = {
        "name": "GOOG",
        "shares": 100,
        "price": 490.10
    }
    print(stock)
    # Upotreba
    name = stock["name"]
    print(name)
    value = stock["shares"] * stock["price"]
    print(value)
    # Upis vrednosti
    stock["shares"] = 75

    stock["date"] = "June 7, 2007"
    print(stock)

    # Mogu se koristiti za brzo pronalaženje podataka
    prices = {
        "GOOG": 490.10,
        "AAPL": 123.50,
        "IBM":  91.50,
        "MSFT": 52.13
    }
    # Default vrednosti
    if "SCOX" in prices:
        p = prices["SCOX"]
    else:
        p = 0.0
    # ili kraće
    p = prices.get("SCOX",0.0)
    # Lista ključeva
    syms = list(prices)     # syms = ["AAPL", "MSFT", "IBM", "GOOG"]
    print(syms)
    # ili
    syms = prices.keys()
    print(syms)

    for key in prices:
        print(key, prices[key])


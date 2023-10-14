print("Ime modula primer2.py: ", __name__)


def if_uslov():
    a = 10
    b = 20
    if a < b:
        print("Computer says Yes")
    else:
        print("Computer says No")

    print("Computer says Yes" if a < b else "Computer says No")


def provera_tipa(suffix):
    if suffix == ".html":
        content = "text/html"
    elif suffix == ".jpg":
        content = "image/jpeg"
    elif suffix == ".png":
        content = "image/png"
    else:
        raise RuntimeError(
            "Unknown content type")
    return content


if __name__ == '__main__':
    if_uslov()

    print(provera_tipa(".html"))

    try:
        provera_tipa(".ogg")
    except Exception as e:
        print(e)

from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def build_title(self, text):
        pass

    @abstractmethod
    def build_subtitle(self, text):
        pass

    @abstractmethod
    def build_paragraph(self, text):
        pass

    @abstractmethod
    def build_list(self, items):
        pass

    @abstractmethod
    def build_definition(self, term, definition):
        pass

# HTML builder
class HTMLBuilder(Builder):
    def build_title(self, text):
        return f"<h1>{text}</h1>"

    def build_subtitle(self, text):
        return f"<h2>{text}</h2>"

    def build_paragraph(self, text):
        return f"<p>{text}</p>"

    def build_list(self, items):
        item_list = "".join([f"<li>{item}</li>" for item in items])
        return f"<ul>{item_list}</ul>"

    def build_definition(self, term, definition):
        return f"<dt>{term}</dt><dd>{definition}</dd>"

class MDBuilder(Builder):
    def build_title(self, text):
        return f"# {text}\n"

    def build_subtitle(self, text):
        return f"## {text}\n"

    def build_paragraph(self, text):
        return f"{text}\n"

    def build_list(self, items):
        item_list = "\n".join([f"- {item}" for item in items] + [""])
        return item_list

    def build_definition(self, term, definition):
        return f"**{term}** - {definition}"

class Director:
    def __init__(self, builder: Builder):
        self.builder = builder

    def construct_homepage(self) -> str:
        out = ""
        out += self.builder.build_title("Ethereum")
        out += self.builder.build_paragraph("Welcome to the Ethereum ecosystem!")
        return out

    def construct_profile_page(self) -> str:
        out = ""
        out += self.builder.build_title("Profile")

        out += self.builder.build_subtitle("Personal information")
        out += self.builder.build_paragraph("Name: Joe")
        out += self.builder.build_paragraph("Lastname: Shooter")

        out += self.builder.build_subtitle("Balance")
        out += self.builder.build_paragraph("Tokens:")
        out += self.builder.build_list(["ETH", "USDT", "SOL"])
        out += self.builder.build_definition("Note", "Do not share your private key!")

        return out

class Client:
    def __init__(self, director: Director):
        self.director = director

    def show_homepage(self):
        print(self.director.construct_homepage())

    def show_profile_page(self):
        print(self.director.construct_profile_page())


if __name__ == '__main__':
    client = Client(Director(HTMLBuilder()))
    client.show_homepage()
    client.show_profile_page()

    client.director.builder = MDBuilder()
    client.show_homepage()
    client.show_profile_page()
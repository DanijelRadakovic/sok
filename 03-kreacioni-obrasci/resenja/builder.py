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
        return f"#{text}"

    def build_subtitle(self, text):
        return f"## {text}"

    def build_paragraph(self, text):
        return text

    def build_list(self, items):
        item_list = "\n".join([f"- {item}" for item in items])
        return item_list

    def build_definition(self, term, definition):
        return f"**{term}** - {definition}"

class Director:
    def construct_doc(self, builder):
        out = ""
        out += builder.build_title("Ovo je naslov")
        out += builder.build_subtitle("Ovo je neki podnaslov")
        out += builder.build_paragraph("Ovo je neki paragraph")
        out += builder.build_list(["Stavka 1", "Stavka 2", "Stavka 3"])
        out += builder.build_definition("Pojam 1", "Ovo je definicija pojma 1")
        out += builder.build_definition("Pojam 2", "Ovo je definicija pojma 2")
        return out

class Client:
    def do_something(self):
        dir = Director()
        html_builder = HTMLBuilder()
        md_builder = MDBuilder()
        doc1 = dir.construct_doc(html_builder)
        print(doc1)
        doc2 = dir.construct_doc(md_builder)
        print(doc2)

if __name__ == '__main__':
    client = Client()
    client.do_something()

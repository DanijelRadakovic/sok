class Person:
    def __init__(self, first_name, last_name, age=None, address=None, phone=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email

class PersonBuilder:
    def __init__(self, first_name, last_name):
        self.person = Person(first_name, last_name)

    def with_age(self, age):
        self.person.age = age
        return self

    def with_address(self, address):
        self.person.address = address
        return self

    def with_phone(self, phone):
        self.person.phone = phone
        return self

    def with_email(self, email):
        self.person.email = email
        return self

    def build(self):
        return self.person

if __name__ == '__main__':

    person1 = PersonBuilder("John", "Doe").with_age(30).with_address("123 Main St").with_phone("555-1234").build()
    person2 = PersonBuilder("Alice", "Smith").with_email("alice@example.com").build()

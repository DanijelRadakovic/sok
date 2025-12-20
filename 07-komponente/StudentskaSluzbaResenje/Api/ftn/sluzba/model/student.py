from .fakultet import Fakultet

class Student(object):

    def __init__(self,**kwargs):
        self.__indeks = kwargs.get('indeks', None)
        self.__ime=kwargs.get('ime',None)
        self.__prezime = kwargs.get('prezime', None)
        self.__email = kwargs.get('email', None)
        self.__fakultet = kwargs.get('fakultet',None)


    @property
    def indeks(self):
        return self.__indeks

    @indeks.setter
    def indeks(self, vrednost):
        if isinstance(vrednost, str):
            self.__indeks = vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, vrednost):
        if isinstance(vrednost, str):
            self.__ime = vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, vrednost):
        if isinstance(vrednost, str):
            self.__prezime = vrednost
        else:
            raise TypeError('Mora biti tipa string')


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, vrednost):
        if isinstance(vrednost, str):
            self.__email = vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def fakultet(self):
        return self.__fakultet

    @fakultet.setter
    def fakultet(self, vrednost: Fakultet):
        if isinstance(vrednost, Fakultet):
            self.__fakultet = vrednost
        else:
            raise TypeError('Mora biti tipa Fakultet')

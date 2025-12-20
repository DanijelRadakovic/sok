from typing import List

from ftn.sluzba.model.student import Student
from ftn.sluzba.model.fakultet import Fakultet
from ftn.sluzba.services.student import StudentUcitatiBase


class StudentiUcitavanjeKod(StudentUcitatiBase):
    def identifier(self):
        return "StudentiUcitavanjeKod"

    def name(self):
        return "Ucitavanje studenata u kodu"

    def ucitati_studente(self, lista_fakulteta: List[Fakultet]):
        return [
            Student(indeks="E12345",
                    ime="Neda",
                    prezime="Nedic",
                    email="email1@gmail.com",
                    fakultet=lista_fakulteta[0] if len(lista_fakulteta) > 0 else None),
            Student(indeks="H4578",
                    ime="Petar",
                    prezime="Petrovic",
                    email="email1@gmail.com",
                    fakultet=lista_fakulteta[1] if len(lista_fakulteta) > 0 else None)
        ]

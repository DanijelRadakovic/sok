import os
import sys
from typing import List

from ftn.sluzba.model.student import Student
from ftn.sluzba.model.fakultet import Fakultet
from ftn.sluzba.services.student import StudentUcitatiBase

studentiTxt = os.path.join(sys.prefix, 'fajlovi/studenti.txt')

def ucitatiStudente(fajl, lista_fakulteta: List[Fakultet]):
    studenti=[]
    with open(fajl,"r") as f:
        for line in f.readlines():
            atributi=line.split("|")
            s=Student()
            s.indeks = atributi[0]
            s.ime = atributi[1]
            s.prezime = atributi[2]
            s.email = atributi[3]
            for fakulet in lista_fakulteta:
                if atributi[4] == fakulet.oznaka:
                    s.fakultet = fakulet
            studenti.append(s)
    return studenti

class StudentiUcitavanjeFajl(StudentUcitatiBase):
    def identifier(self):
        return "StudentiUcitavanjeFajl"

    def name(self):
        return "Ucitavanje studenata iz fajla"

    def ucitati_studente(self, lista_fakulteta: List[Fakultet]):
        return ucitatiStudente(studentiTxt, lista_fakulteta)
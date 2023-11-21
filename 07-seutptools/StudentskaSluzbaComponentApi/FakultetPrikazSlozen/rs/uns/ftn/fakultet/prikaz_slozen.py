from typing import List

from rs.uns.ftn.studentska.sluzba.model.fakultet import Fakultet
from rs.uns.ftn.studentska.sluzba.services.fakultet import FakultetPrikazBase


class FakultetPrikazSlozen(FakultetPrikazBase):
    def identifier(self):
        return "FakultetPrikazSlozen"

    def name(self):
        return "Prikaz svih atributa fakulteta"

    def prikazati_fakultete(self, lista_fakulteta: List[Fakultet]):
        prikaz = "{:10}|{:40}|{:40}\n".format("Oznaka", "Naziv", "Adresa")
        for f in lista_fakulteta:
            prikaz += "{:10}|{:40}|{:40}\n".format(f.oznaka, f.naziv, f.adresa)
        return prikaz

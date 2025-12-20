from typing import List

from ftn.sluzba.model.fakultet import Fakultet
from ftn.sluzba.services.fakultet import FakultetPrikazBase

class FakultetPrikazObican(FakultetPrikazBase):
    def identifier(self):
        return "FakultetPrikazObican"

    def name(self):
        return "Prikaz samo naziva fakulteta"

    def prikazati_fakultete(self, lista_fakulteta: List[Fakultet]):
        prikaz = f"Naziv\n"
        for f in lista_fakulteta:
            prikaz += f"{f.naziv}\n"
        return prikaz

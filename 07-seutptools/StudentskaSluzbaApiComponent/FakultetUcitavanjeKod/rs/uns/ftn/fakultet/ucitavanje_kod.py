from typing import List

from rs.uns.ftn.studentska.sluzba.model.fakultet import Fakultet
from rs.uns.ftn.studentska.sluzba.services.fakultet import FakultetUcitatiBase


class FakultetUcitavanjeKod(FakultetUcitatiBase):
    def identifier(self):
        return "FakultetUcitatiKod"

    def name(self):
        return "Ucitavanje fakulteta u kodu"

    def ucitati_fakultete(self) -> List[Fakultet]:
        fakulteti = []

        fakulteti.append(
            Fakultet(oznaka="0123",
                     naziv="Fakultet Tehnickih nauka",
                     adresa="Trg Dositeja Obradovica 6"))
        fakulteti.append(
            Fakultet(oznaka="2345",
                     naziv="Prirodno matematicki fakultet",
                     adresa="Trg Dositeja Obradovica 2-4"))

        return fakulteti

from typing import List

from ftn.sluzba.model.fakultet import Fakultet
from ftn.sluzba.services.fakultet import FakultetUcitatiBase


class FakultetUcitavanjeKod(FakultetUcitatiBase):
    def identifier(self):
        return "FakultetUcitatiKod"

    def name(self):
        return "Ucitavanje fakulteta u kodu"

    def ucitati_fakultete(self) -> List[Fakultet]:
        return [
            Fakultet(oznaka="0123",
                     naziv="Fakultet Tehnickih nauka",
                     adresa="Trg Dositeja Obradovica 6"),
            Fakultet(oznaka="2345",
                     naziv="Prirodno matematicki fakultet",
                     adresa="Trg Dositeja Obradovica 2-4")
        ]

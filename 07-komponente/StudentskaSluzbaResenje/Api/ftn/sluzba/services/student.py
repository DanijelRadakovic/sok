from abc import abstractmethod
from typing import List

from .fakultet import ServiceBase
from ..model.student import Student
from ..model.fakultet import Fakultet


class StudentUcitatiBase(ServiceBase):
    @abstractmethod
    def ucitati_studente(self, lista_fakulteta: List[Fakultet]) -> List[Student]:
        pass


class StudentPrikazBase(ServiceBase):
    @abstractmethod
    def prikazati_studente(self, lista_studenata: List[Student]):
        pass
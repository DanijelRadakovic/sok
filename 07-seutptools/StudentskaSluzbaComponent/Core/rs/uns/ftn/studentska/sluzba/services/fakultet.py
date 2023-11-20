from abc import ABC, abstractmethod
from typing import List

from .model import Fakultet


class ServiceBase(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass


class FakultetUcitatiBase(ServiceBase):

    @abstractmethod
    def ucitati_fakultete(self) -> List[Fakultet]:
        pass


class FakultetPrikazBase(ServiceBase):

    @abstractmethod
    def prikazati_fakultete(self, lista_fakulteta: List[Fakultet]):
        pass

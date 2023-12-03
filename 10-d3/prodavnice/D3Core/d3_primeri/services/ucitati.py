from abc import abstractmethod, ABC


class UcitatiService(ABC):
    @abstractmethod
    def naziv(self):
        pass

    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def ucitati(self):
        pass
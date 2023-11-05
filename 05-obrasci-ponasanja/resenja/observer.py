from abc import ABC, abstractmethod
from typing import List


class Observable(ABC):
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def delete_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for obs in self.observers:
            obs.update()


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class PritisakPrikaz(Observer):
    def __init__(self, merac_pritiska):
        self.merac_pritiska: MeracPritiska = merac_pritiska

    def register(self):
        self.merac_pritiska.add_observer(self)

    def update(self):
        print("Prikaz pritiska:", self.merac_pritiska.uzmi_pritisak())


class SigurnosniVentil(Observer):
    def __init__(self, merac_pritiska):
        self.merac_pritiska: MeracPritiska = merac_pritiska
        self.opened = False
        self.limit = 80

    def register(self):
        self.merac_pritiska.add_observer(self)

    def update(self):
        if self.opened:
            return
        if self.merac_pritiska.uzmi_pritisak() > self.limit:
            self.opened = True
            print("Sigurnosni ventil otvoren")


class MeracPritiska(Observable):
    def __init__(self):
        super().__init__()
        self.pritisak = 0

    def uzmi_pritisak(self):
        return self.pritisak

    def podesi_pritisak(self, novi_pritisak):
        self.pritisak = novi_pritisak
        self.notify()  # Obaveštavamo observe o promeni pritiska


def client():
    merac = MeracPritiska()
    ventil = SigurnosniVentil(merac)
    prikaz = PritisakPrikaz(merac)

    ventil.register()
    prikaz.register()

    merac.podesi_pritisak(50)
    merac.podesi_pritisak(90)
    merac.podesi_pritisak(70)


if __name__ == "__main__":
    client()

from abc import ABC, abstractmethod


# Abstract Base Class example
class Drawable(ABC):

    @abstractmethod
    def draw(self):
        pass


# Property example
class Point(Drawable):

    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y


    @property
    def x(self) -> float:
        return self._x


    @x.setter
    def x(self, x: float) -> None:
        self._x = x


    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, y: float) -> None:
        self._y = y


    def draw(self):
        print("X:", self._x, "Y:", self._y)


if __name__ == "__main__":
    # Property and ABC demon
    point = Point(2.0, 2.0)
    point.draw()
    # baca gresku
    # abs = Drawable()

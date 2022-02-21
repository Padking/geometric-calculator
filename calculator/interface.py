from abc import (
    ABC,
    abstractmethod,
)


class ShapeInterface(ABC):

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...

    @abstractmethod
    def volume(self):
        ...

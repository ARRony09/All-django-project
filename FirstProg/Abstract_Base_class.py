# from abc import ABCMeta,abstractmethod
from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class rectangle(shape):
    types = "Rectangle"
    sides =4

    def __init__(self):
        self.length =6
        self.wide =5

    def print_area(self):
        return self.length * self.wide

rec1 = rectangle()
print(rec1.print_area())

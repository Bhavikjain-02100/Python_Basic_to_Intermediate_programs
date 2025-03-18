from abc import abstractmethod, ABC
#ABC stand for Abstract Base Class

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Print my own")

lp=Laptop()
lp.process()

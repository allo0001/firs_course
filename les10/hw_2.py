from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        self.consumption = self.fabric_consumption()

    def fabric_consumption(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        self.consumption = self.fabric_consumption()

    def fabric_consumption(self):
        return 2*self.height + 0.3


c1 = Coat(54)
c2 = Suit(190)

print(c1.consumption + c2.consumption)

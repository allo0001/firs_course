class Storage:
    def __init__(self, name):
        self.name = name
        self.storage = {}

    def addEquipment(self, equipment):
        self.storage[equipment.serialNumber] = {'model': equipment.model, 'type': equipment.__class__.__name__ }

    def send_to_divisions(self, serialNumber):
        self.storage.pop(serialNumber)



class Equipment:
    def __init__(self, model, serialNumber):
        self.model = model
        self.serialNumber = serialNumber

    def stored(self, storage):
        storage.addEquipment(self)


class Printer(Equipment):
    def __init__(self, model, serialNumber, color: bool):
        super().__init__(model, serialNumber)
        self.color = color


class Scanner(Equipment):
    def __init__(self, model, serialNumber, speed: int):
        super().__init__(model, serialNumber)
        self.speed = speed


class Copier(Equipment):
    def __init__(self, model, serialNumber, color: int):
        super().__init__(model, serialNumber)
        self.color = color


s1 = Storage('st1')
pr1 = Printer('e122', '1', True)
sc1 = Scanner('s12', '2', 12)
c1 = Copier('c11', '3', False)

print(s1.storage)
pr1.stored(s1)
print(s1.storage)
sc1.stored(s1)
c1.stored(s1)
print(s1.storage)
s1.send_to_divisions('1')
print(s1.storage)

# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__(self.__class__.__name__)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент - {self.title}')


class Pencil(Stationery):
    def __init__(self):
        super().__init__(self.__class__.__name__)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент - {self.title}')


class Handle(Stationery):
    def __init__(self):
        super().__init__(self.__class__.__name__)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент - {self.title}')


stationery = Stationery('Stationery')
pen = Pen()
pencil = Pencil()
handle = Handle()

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()

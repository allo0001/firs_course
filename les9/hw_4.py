class Car:
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police  = bool(is_police)
        
    def go(self):
        print('Машина поехала')
        
    def stop(self):
        print('Машина остановилась')
        
    def turn(self, direction):
        print(f'Машина повернула на {direction}')
        
    def show_speed(self):
        print(f'Скорость автомобиля - {self.speed}')
        

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля - {self.speed} \nПревышение скорости на {self.speed - 60}')
        else:
            print(f'Скорость автомобиля - {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля - {self.speed} \nПревышение скорости на {self.speed - 40}')
        else:
            print(f'Скорость автомобиля - {self.speed}')
            
            
car1 = SportCar(200,'red','car1', 0)
car2 = WorkCar(150,'green','car2', 0)

car1.go()
print()
car1.stop()
print()
car1.turn('left')
print()
car1.show_speed()
print()
car2.show_speed()

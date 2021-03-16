class Worker:
    
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income
        
    def get_income(self):
        return self.__income
        
    
class Position(Worker):
    
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    
    def get_total_income(self):
        return self.get_income()["wage"] + super().get_income()["bonus"]

    
worker = Position('Иван', 'Иванов', 'слесарь', {"wage": 50, "bonus":25})

print(f'name - {worker.name}')
print(f'surname - {worker.surname}')
print(f'position - {worker.position}')

print(f'get_full_name - {worker.get_full_name()}')
print(f'get_total_income - {worker.get_total_income()}')

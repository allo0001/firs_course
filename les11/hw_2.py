class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text
        
        
a = int(input('Введите a:'))
b = int(input('Введите b:'))

try:
    if b == 0:
        raise ZeroDivision('\nДеление на ноль недопустимо')
    print(f'a / b = {a/ b}')

except ZeroDivision as err:
    print(err)
    
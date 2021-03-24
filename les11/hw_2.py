class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text
        
        
a = int(input('Ввежите a:'))
b = int(input('Ввежите b:'))

try:
    if b == 0:
        raise ZeroDivision('\nДеление на 0')
    print(f'a / b = {a/ b}')

except ZeroDivision as err:
    print(err)
    
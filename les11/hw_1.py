import re


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def pars(cls, date):
        if d := cls.valid(date):
            return map(int, d.split('-'))

    @staticmethod
    def valid(date):
        if re.match(r'^\d{4}(-\d{2}){2}$', date):
            y, m, d = map(int, date.split('-'))
            if 2100 >= y >= 1900 and 0 < m < 13 and 0 < d < 31:
                return date
            else:
                print('Ошибка формата даты.')
                return False
        else:
            print('Ошибка формата даты.')
            return False


d1 = '2021-05-26'
d2 = '2021-05-26'

print(Date.valid('2021-05-01'))
print(*Date.pars('2021-05-01'))

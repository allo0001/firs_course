from util import currency_rates
import sys


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        val = currency_rates(arg)
        if val:
            print(f'Курс {arg.upper()} на {val[1]} - {val[0]}')
        else:
            print(val)
        print('*'*35)

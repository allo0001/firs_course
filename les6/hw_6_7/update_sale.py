import sys


def show_sale(path):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            s = f.readline()
            if s:
                yield s #.replace('\n', '')
            else:
                break


def write_sales(path, sales):
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(sales)


if __name__ == '__main__':
    sales = [i for i in show_sale('bakery.csv')]
    sale_index = int(sys.argv[1])
    new_value = sys.argv[2] + '\n'
    if sale_index > len(sales):
        print('Вы ввели не верный индекс редактируемого элемента!!!')
    else:
        sales[sale_index] = new_value
    write_sales('bakery.csv', sales)

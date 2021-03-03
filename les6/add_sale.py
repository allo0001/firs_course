import sys

def add_sale(path, sale):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(sale + '\n')
        

if __name__ == '__main__':
    add_sale('bakery.csv', sys.argv[1])
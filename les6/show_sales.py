import sys

def show_sale(path):
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            s = f.readline()
            if s:
                yield s.replace('\n', '')
            else:
                break
        

if __name__ == '__main__':
    if len(ar := sys.argv) == 1:
        print(*[i for i in show_sale('bakery.csv')], sep='\n')
    elif len(ar) == 2:
        print(*[i for i in show_sale('bakery.csv')][int(ar[1])-1:], sep='\n')
    else:
        print(*[i for i in show_sale('bakery.csv')][int(ar[1])-1:int(ar[2])], sep='\n')
import re


class NotNumeric(Exception):
    def __init__(self, text):
        self.text = text


num = re.compile(r'^[-+]?\d+[,.]?\d*$')
result = []

while True:
    try:
        el = input('Введите элемент списка(число): ')
        if el.lower() == 'stop':
            break
        elif num.match(el):
            result.append(el)
        else:
            raise NotNumeric('Число число')
    except NotNumeric as err:
        print(err)
print(result)

from requests import get, utils
from decimal import Decimal
import xml.etree.ElementTree as ET

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
response = response.content.decode(encoding=encodings)


def parse_response_str():
    split_res = response.split('</Valute>')
    split_res.pop(-1)
    rez = {}
    for valute in split_res:
        char_code = valute[valute.find('<CharCode>')+10: valute.find('<CharCode>')+13]
        value = Decimal(valute[valute.find('<Value>')+7: valute.find('<Value>')+14].replace(',', '.'))
        nominal = int(valute[valute.find('<Nominal>')+9: valute.find('<Nominal>')+13].replace('<', '').replace('/', '').replace('N', ''))
        rez[char_code] = {'value': value, 'nominal': nominal}
    return rez


def parse_response_xml():
    rez = {}
    root_node = ET.ElementTree(ET.fromstring(response)).getroot()
    for elem in root_node.findall('Valute'):
        char_code = elem.find('CharCode').text
        value = Decimal(elem.find('Value').text.replace(',', '.'))
        nominal = int(elem.find('Nominal').text)
        rez[char_code] = {'value': value, 'nominal': nominal}
    return rez


def currency_rates(char_code, function=parse_response_xml):
    char_code = char_code.upper()
    res = function()
    valute = res.get(char_code)
    if valute:
        rez = valute['value'] / valute['nominal']
        return rez
    else:
        return valute
    
    
if __name__ == '__main__':
    # парсинг через методы строк
    print('Курс USD - ', currency_rates('USD', function=parse_response_str))
    # парсинг модулем xml
    print('Курс EUR - ', currency_rates('eur'))

from requests import get, utils
from decimal import Decimal
import xml.etree.ElementTree as ET
from datetime import date

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
response = response.content.decode(encoding=encodings)


def parse_response_str():
    split_res = response.split('</Valute>')
    split_res.pop(-1)
    rez = {}
    date_res = split_res[0][split_res[0].find('Date')+6: split_res[0].find('Date')+16].split('.')
    date_res = list(map(int, date_res))
    rez['Date'] = date(date_res[2], date_res[1], date_res[0])
    for valute in split_res:
        char_code = valute[valute.find('<CharCode>')+10: valute.find('<CharCode>')+13]
        value = Decimal(valute[valute.find('<Value>')+7: valute.find('<Value>')+14].replace(',', '.'))
        nominal = int(valute[valute.find('<Nominal>')+9: valute.find('<Nominal>')+13].replace('<', '').replace('/', '').replace('N', ''))
        rez[char_code] = {'value': value, 'nominal': nominal}
    return rez


def parse_response_xml():
    rez = {}
    root_node = ET.ElementTree(ET.fromstring(response)).getroot()
    date_res = root_node.get('Date').split('.')
    date_res = list(map(int, date_res))
    rez['Date'] = date(date_res[2], date_res[1], date_res[0])
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
    date_res = res.get('Date')
    if valute:
        rez = (valute['value'] / valute['nominal'], date_res)
        return rez
    else:
        return None
    
    
if __name__ == '__main__':
    # парсинг через методы строк
    val = currency_rates('USD', function=parse_response_str)
    if val:
        print(f'Курс USD на {val[1]} - {val[0]}')
    else: 
        print(val)    
    # парсинг модулем xml
    val = currency_rates('eur')
    if val:
        print(f'Курс EUR на {val[1]} - {val[0]}')
    else:    
        print(val)

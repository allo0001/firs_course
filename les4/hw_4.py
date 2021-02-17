from util import currency_rates, parse_response_str

# парсинг через методы строк
val = currency_rates('ew', function=parse_response_str)
print(f'Курс USD на {val[1]} - {val[0]}')
# парсинг модулем xml
val = currency_rates('eur')
print(f'Курс EUR на {val[1]} - {val[0]}')

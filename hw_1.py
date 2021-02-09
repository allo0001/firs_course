
duration = int(input('Введите количество секунд: '))

d = 0
h = 0
m = 0
s = 0

if (duration // 86400 > 0):
    d = duration // 86400
    duration = duration % 86400 

if (duration // 3600 > 0):
    h = duration // 3600
    duration = duration % 3600     

if (duration // 60 > 0):
    m = duration // 60
    s = duration % 60    
else:
    s = duration

if d:
    print(f'{d} дн {h} час {m} мин {s} сек')
elif h:
    print(f'{h} час {m} мин {s} сек')
elif m:
    print(f'{m} мин {s} сек')
elif s:
    print(f'{s} сек')    


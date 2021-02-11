mes = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i,m in enumerate(mes):
    if m.isdigit():
        if len(m) == 1:
            mes[i] = f'"0{m}"'
        else:
            mes[i] = f'"{m}"'
    elif m[0] == '+' or m[0] == '-':
        if len(m) == 2:
            mes[i] = f'"{m[0]}0{m[1]}"'
        else:
            mes[i] = f'"{m}"'

print (' '.join(mes))       

    

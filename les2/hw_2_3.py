mes = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i,m in enumerate(mes):
    if m.isdigit():
        mes[i] = f'"{int(m):02d}"'
        
    elif m[0] == '+' or m[0] == '-':
        if m[1:].isdigit(): 
            mes[i] = f'"{m[0]}{int(m[1:]):02d}"'
  
print (' '.join(mes))       

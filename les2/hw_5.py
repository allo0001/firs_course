prices = [57.8, 46.01, 97, 8.56, 86.84,
          75.66, 35, 65, 45.35, 46.3,
          78.5, 53.6, 58, 48, 99.99,
          57, 82.6, 66.3, 44.1, 22.2]
#A
print("*******A*******")
rez = []

for price in prices:
    price = float(price)
    r = int(price)
    k = round((price % 1) * 100)
    rez.append(f'{r} руб {k:02d} коп')
        
print (', '.join(rez))
#B
print("*******B*******")
print(sorted(prices))
print(prices)

#C
print("*******C*******")
pricesSort = sorted(prices,reverse=True)
print(pricesSort)

#D
print("*******D*******")
print(pricesSort[:5])

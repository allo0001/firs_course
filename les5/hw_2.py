n = int(input('введите n :'))

odd_to_n = (num for num in range(1, n+1, 2))

for i in odd_to_n:
    print(i)

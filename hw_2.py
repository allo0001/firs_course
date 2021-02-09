
odd = []
sum1 = 0
sum2 = 0

for n in range(1,1001,2):
    odd.append(n**3)

for i,n in enumerate(odd):
    s = 0
    while n > 0:
        s += n%10
        n = n//10
        
    if s%7 == 0:
       sum1 += odd[i]
    
    odd[i] += 17

for i,n in enumerate(odd):
    s = 0
    while n > 0:
        s += n%10
        n = n//10
        
    if s%7 == 0:
        sum2 += odd[i]

print(sum1)
print(sum2)
    
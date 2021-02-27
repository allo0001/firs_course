from time import time
from random import randint

#src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src = [randint(1, 500) for i in range(1000)]

#решение "в лоб"
start = time()
result = [n for n in src if src.count(n) == 1]
print(result)
print(time() - start)

#ускоренное решение "в лоб"
start = time()
s = set()
u = [x for x in src if x not in s and not s.add(x)]
result = [n for n in u if src.count(n) == 1]
print(result)
print(time() - start)

#решение без count()
start = time()
src2 = src.copy()
s = set(src2)
for n in s:
    src2.remove(n)
s = s - set(src2)
print([res for res in src if res in s])
print(time() - start)



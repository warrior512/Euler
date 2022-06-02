# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
l = []
k = []
for i in range(100, 1000):
    for i2 in range(100, 1000):
        d = i * i2
        l.append(d)               
for x in l:
    a = list(str(x))
    b = list(str(x))
    b.reverse()
    if a == b:
        k.append(x)
k.sort()
u = k[-1]
print(u)

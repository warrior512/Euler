def IsPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

h = 1
n = 2
while h <= 10001:
    n += 1
    if IsPrime(n):
        h += 1
print(n)
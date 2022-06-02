# Найдите сумму всех простых чисел меньше двух миллионов.

# Find the sum of all the primes below two million.

#142913828923

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

i = 0
j = 0
while i < 2000000:
    if isPrime(i):
        j += i
    i += 1
print(j-1)
# Наибольший простой делитель 600851475143

# What is the largest prime factor of the number 600851475143 ?

x = 600851475143
l = []
i = 2
a = 2
while  x != 1:
    if x % a == 0:
        x /= a
        l.append(a)
        a = 2
    else:
        a += 1
l.sort()
l.pop(0)
u = 1
for t in l:
    u *= t
print(u)
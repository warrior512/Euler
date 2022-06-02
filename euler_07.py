# Какое число является 10001-м простым числом?

# What is the 10 001st prime number?
h = 1
j = 3
def prst(x):    
    for i in range(2, x):
        if x % i == 0:
            y = 'ne prostoe'
            # print(y)
            break
        elif x % i != 0:
            y = 'prostoe'
        # print(y)
    if y == 'prostoe':
        return 1
    else:
        return 2

while h < 10001:
    if prst(j) == 1:
        h += 1
        j += 1
    elif prst(j) ==2:
        j += 1
        
print(h)
        

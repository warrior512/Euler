j = 0
l = 0
p = []
while True:
    j += 1
    l += j
    
    for i in range(1,l+1):
        if l % i == 0:
            
            p.append(i)
      
            
    if len(p) > 500:
        print(p)
        print(l)
        break
    p = []
    print(l)
            
print(l)
            

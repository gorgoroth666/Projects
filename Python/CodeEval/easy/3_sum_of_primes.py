import math


def isPrime(p):
    if p <= 1:
        return False
    if p == 2:
        return True        
    if p % 2 == 0:
        return False
        
    for k in range(3, int(p**0.5) + 1, 2):
        if p % k == 0:
            return False

    return True    
    
    
    
i = 0
n = 0
l = []
while n < 1000:
    i += 1
    if isPrime(i):
        n += 1
        l.append(i)

print(sum(l))        
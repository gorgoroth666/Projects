      
import sys


def sum_square_digits(n):
    return sum(int(c)**2 for c in str(n))
        

def isHappyNumber(i):  
    l = []    
    n = i
    l.append(n)
    while n!=1:        
        n = sum_square_digits(n)
        if n in l:
            return 0 #endless loop
        l.append(n)
    
    
    if n == 1:
        return 1
    return 0


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
   
    print(isHappyNumber(int(test)))

test_cases.close()

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)
    
    
import sys

if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n")
    print(fibo(int(test)))


test_cases.close()
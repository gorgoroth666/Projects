import sys

def smallest_multiple(x,n):
    i = 1
    while( x > n * i):
        i += 1
    return n * i

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    args = test.split(",")
    print(smallest_multiple(int(args[0]), int(args[1])))


test_cases.close()

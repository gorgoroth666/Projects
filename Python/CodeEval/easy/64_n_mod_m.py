import sys

def mod(n, m):
    d = n // m
    return n - d*m


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
    l = test.split(",")
    
    print(mod(int(l[0]), int(l[1])))


test_cases.close()
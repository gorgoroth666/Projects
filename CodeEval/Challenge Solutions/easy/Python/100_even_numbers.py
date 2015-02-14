import sys
import math


def is_even(n):
    return 1 if n % 2 == 0 else 0


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    test = test.strip(" ")
    if test == "":
        continue
    
    l.append(test)
  
test_cases.close()



for s in l:

    print(is_even(int(s)))
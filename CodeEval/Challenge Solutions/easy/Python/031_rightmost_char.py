     
import sys

def rightmost_char(s, c):
    for i in range(len(s)-1, -1, -1):
        if s[i] == c:
            return i
    return -1


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
    l = test.split(",")    
    print(rightmost_char(l[0], l[1]))

test_cases.close()

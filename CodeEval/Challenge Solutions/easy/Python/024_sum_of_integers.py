    
import sys

if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    l.append(int(test))

print(sum(l))
test_cases.close()
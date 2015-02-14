    
import sys

def intersection(l1, l2):
    a = set(l1)
    b = set(l2)
    return list(a & b)


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip("\n")
    lists = test.split(";")
    l1 = lists[0].split(",")
    l2 = lists[1].split(",")
    l3 = intersection(l1, l2)
    v = [int(s) for s in l3]
    v.sort()
    w = [str(i) for i in v]
    print(",".join(w))

test_cases.close()

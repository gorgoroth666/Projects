    
import sys

def unique_element(l):
    return list(set(l))


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip("\n")
    l = test.split(",")
    if len(l) == 1:
        if l != ['']:
            print(l[0])
        continue
    v = [int(s) for s in l]
    u = unique_element(v)
    u.sort()
    w = [str(i) for i in u]
    print(",".join(w))

test_cases.close()

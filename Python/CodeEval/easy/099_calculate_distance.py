import sys
import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


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
    for c in "(),":
        s = s.replace(c, "")
    parts = s.split(" ")
    x1 = int(parts[0])
    y1 = int(parts[1])
    x2 = int(parts[2])
    y2 = int(parts[3])
    print(int(distance(x1, y1, x2, y2)))
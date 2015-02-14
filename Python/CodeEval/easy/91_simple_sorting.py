import sys


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
    
    l.append(test)
  
test_cases.close()



for s in l:
    to_sort = []
    for d in s.split(" "):
        to_sort.append(float(d))
    u = ["{:.3f}".format(f) for f in sorted(to_sort)]
    print(" ".join(u))
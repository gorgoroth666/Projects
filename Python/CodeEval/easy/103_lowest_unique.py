import sys


def is_unique(x, l):
    return l.count(x) == 1

def lowest_unique(l):
    m = 9
    mi = 0
    for i in range(len(l)):
        if is_unique(l[i], l) and l[i] < m:
            m = l[i]
            mi = i + 1
    
    return mi
    


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
    arg = []
    for i in s.split(" "):
        arg.append(int(i))
    print(lowest_unique(arg))
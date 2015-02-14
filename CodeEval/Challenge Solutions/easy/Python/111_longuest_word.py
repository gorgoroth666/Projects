import sys

def longuest_word(l):
    m = 0
    mi = -1
    for w in range(len(l)):
        if len(l[w]) > m:
            m = len(l[w])
            mi = w
    return l[mi]
            
            
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
    print(longuest_word(s.split(" ")))
    
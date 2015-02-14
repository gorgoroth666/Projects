import sys

def is_repetition(s, ss):
    u = len(s)
    v = len(ss)
    if u % v != 0:
        return False
    if s == ss * (u // v):
        return True
    return False

def shortest_repetition(s):
    for i in range(1, len(s)+1):
        if is_repetition(s, s[0:i]):
            return s[0:i]
    return ""
    

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
    print(len(shortest_repetition(s)))
    
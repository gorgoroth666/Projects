import sys
from operator import itemgetter



def maxBeautiful(s):
    n = len(set(s))
    m = {}
    for c in s:
        m[c] = s.count(c)
        
    p = sorted(m.items(), key=itemgetter(1), reverse=True)
    summation = 0
    value = 26
    for tuple in p:
        summation += tuple[1] * value
        value -= 1
        
    return summation

if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
    
    test = test.lower()
    for c in ":!^_-=+(), .;?/§[]&0123456789":
        test = test.replace(c, "")
    
    other = ""
    for c in test:
        if c > 'z' or c < 'a':
            continue
        other += c
            
    
    l.append(other)
  
test_cases.close()

for s in l:
    print(maxBeautiful(s))
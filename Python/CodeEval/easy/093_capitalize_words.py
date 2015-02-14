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
    args = s.split(" ")
    result = []
    for arg in args:
        
        result.append(arg[0].upper() + arg[1:])
        
    
    print(" ".join(result))
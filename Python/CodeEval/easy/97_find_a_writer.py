import sys


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
    parts = s.split("|")
    codes = parts[1].strip(" ").split(" ")
    result = ""

    for c in codes:        
        result += parts[0][int(c)-1]
        
    
    print(result)
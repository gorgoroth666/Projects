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
    result = ""
    for c in s:
        if c <= "z" and c >= "a":
            result += c.upper()
        elif "A" <= c and c <= "Z":
            result += c.lower()
        else:
            result += c
    
    print(result)
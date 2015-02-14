import sys

def isSelfDescribing(n):
    s = str(n)
    for i in range(len(s)):
        if int(s[i]) != s.count(str(i)):
            return 0
    return 1
        


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
   
    print(isSelfDescribing(int(test)))

test_cases.close()

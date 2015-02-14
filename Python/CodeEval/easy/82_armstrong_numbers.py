import sys

def isArmstrongNumber(num):
    s = str(num)
    n = len(s)
    return num == sum(int(c)**n for c in s)

if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
    l.append(int(test))
  
test_cases.close()


for n in l:
    print(isArmstrongNumber(n))
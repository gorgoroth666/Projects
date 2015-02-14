import sys

          
if len(sys.argv) <= 1:
    exit(0)
test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    test = test.strip()
    if test == "":
        continue    
    l.append(test)
test_cases.close()


for s in l:
    args = s.split("|")
    args[0] = args[0].strip()
    args[1] = args[1].strip()
    l0 = args[0].split(" ")
    l1 = args[1].split(" ")
    result = []
    for i in range(len(l0)):
        result.append(str(int(l0[i])*int(l1[i])))
        
    print(" ".join(result))
    
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
    args = s.split(",")
    words = []
    digits = []
    for e in args:
        if e.isdigit():
            digits.append(e)
        else:
            words.append(e)
    if words != [] and digits != []:
        print(",".join(words), "|", ",".join(digits), sep = "")
    else:
        print(",".join(words), ",".join(digits), sep = "")
    
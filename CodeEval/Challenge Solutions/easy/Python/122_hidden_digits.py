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
    hasDigits = False
    for c in s:
        if c.isdigit():
            hasDigits = True
            print(c, end="")
        elif ord(c) in range(ord("a"), ord("j") + 1):
            hasDigits = True
            print(ord(c) - ord("a"), end ="")
    if hasDigits:
        print()
    else:
        print("NONE")
    
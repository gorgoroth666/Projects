import sys



if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
    
    print(int(test, 16))


test_cases.close()
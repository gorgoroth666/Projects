import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n")
    print(test.lower())


test_cases.close()
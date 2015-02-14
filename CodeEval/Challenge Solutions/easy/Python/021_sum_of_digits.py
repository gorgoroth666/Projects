import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n")
    print(sum(int(i) for i in test))


test_cases.close()
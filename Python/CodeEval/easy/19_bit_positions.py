import sys

def same_bits(n, p1, p2):
    s = bin(n)
    if s[::-1][p1-1] == s[::-1][p2-1]:
        return "true"
    return "false"

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n")
    args = test.split(",")
    print(same_bits(int(args[0]), int(args[1]), int(args[2])))


test_cases.close()
import sys

def reverseWords(s):
    s = s.strip("\n")
    return " ".join(s.split(" ")[::-1])
        
        

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(reverseWords(test))


test_cases.close()

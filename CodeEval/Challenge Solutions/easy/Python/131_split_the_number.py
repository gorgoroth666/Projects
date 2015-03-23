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



def code_to_number(num, code):
    """
    Transforms a sequence of letters of the form "abdc"
    to a number. a represents the first digit of num, b the second, ...
    Such as:
    code_to_number("1234", "acb") == 132
    """
    result = 0
    for i in range(len(code)):
        result += int(num[ord(code[i]) - ord('a')]) * 10**(len(code) - i - 1)
    return result
        


for s in l:    
    args = s.split(" ")
    nums = []
    for c in args[0]:
        nums.append(int(c))
    
    if "+" in args[1]:
        operands = args[1].split("+")
    else:
        operands = args[1].split("-")
        
    left_operand = code_to_number(args[0], operands[0])
    right_operand = code_to_number(args[0], operands[1])
    
    if "+" in args[1]:
        print(left_operand + right_operand)
    else:
        print(left_operand - right_operand)

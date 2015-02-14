import sys
   
def convert1(n):
    if len(n) < 1:
        return ""
    v = int(n[-1])
    if v == 0:
        return ""
    if v <= 3:
        return "I" * v
    if v == 4:
        return "IV"
    if v <= 8:
        return "V" + "I" * (v-5)
    if v == 9:
        return "IX"
    
def convert10(n):
    if len(n) < 2:
        return ""
    v = int(n[-2])
    if v == 0:
        return ""
    if v <= 3:
        return "X" * v
    if v == 4:
        return "XL"
    if v <= 8:
        return "L" + "X" * (v-5)
    if v == 9:
        return "XC"
        
def convert100(n):
    if len(n) < 3:
        return ""
    v = int(n[-3])
    if v == 0:
        return ""
    if v <= 3:
        return "C" * v
    if v == 4:
        return "CD"
    if v <= 8:
        return "D" + "C" * (v-5)
    if v == 9:
        return "CM"
        

def convert1000(n):
    if len(n) < 4:
        return ""
    v = int(n[-4])
    if v == 0:
        return ""
    if v <= 3:
        return "M" * v
    return ""
        
        
def to_roman_numerals(n):
    return convert1000(n) + convert100(n) + convert10(n) + convert1(n)
    

if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    test = test.strip(" ")
    if test == "":
        continue
    
    l.append(test)
  
test_cases.close()


for s in l:
    print(to_roman_numerals(s))
    
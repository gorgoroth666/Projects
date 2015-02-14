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
    args = s.split(":")
    args[0] = args[0].strip()
    args[1] = args[1].strip()
    numbers = args[0].split(" ")
    exchanges = args[1].split(",")
    for e in exchanges:
        e = e.strip()
        positions = e.split("-")
        p0 = int(positions[0])
        p1 = int(positions[1])
        temp = numbers[p0]
        numbers[p0] = numbers[p1]
        numbers[p1] = temp
    
    print(" ".join(numbers))
    
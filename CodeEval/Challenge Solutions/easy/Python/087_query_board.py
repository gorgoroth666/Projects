import sys


def setCol(j, x, m):
    for i in range(256):
        m[i][j] = x

        
def setRow(i, x, m):
    for j in range(256):
        m[i][j] = x        
        

def queryRow(i, m):
    return sum(m[i][j] for j in range(256))
        

def queryCol(j, m):
    return sum(m[i][j] for i in range(256))


    
def apply(s, m):    
    args = s.split(" ")
    if args[0] == "SetRow":
        setRow(int(args[1]), int(args[2]), m)
    if args[0] == "SetCol":
        setCol(int(args[1]), int(args[2]), m)
    if args[0] == "QueryRow":
        print(queryRow(int(args[1]), m))
    if args[0] == "QueryCol":
        print(queryCol(int(args[1]), m))
       
        
        


if len(sys.argv) <= 1:
    exit(0)

test_cases = open(sys.argv[1], 'r')
l = []
for test in test_cases:
    test = test.strip("\n")
    if test == "":
        continue
    
    l.append(test)
  
test_cases.close()


m = []
for k in range(256):
    m.append([0] * 256)

# print(m)

for s in l:
    apply(s, m)
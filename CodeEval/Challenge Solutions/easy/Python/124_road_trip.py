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


# Get distances
# Sort them in ascending order
# Print the distance between them

for s in l:
    s = s.strip(";")    
    distances = []
    args = s.split(";")
    for city in args:
        couple = city.split(",")
        distances.append(int(couple[1]))
    distances.sort()

    print(distances[0], end="")
    for i in range(len(distances) - 1):
        print(",", end="")
        print(distances[i+1] - distances[i], end="")

    print()
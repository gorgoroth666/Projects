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


# Read list of int
# count the number of consecutive n starting with the

def count_consecutive(l, i):
    """
    Counts the number of times l[i] is repeated in l
    starting at position i.
    Returns the count and the ending position
    """
    count = 0
    target = l[i]
    while i < len(l) and l[i] == target:
        i += 1
        count += 1 
    return count, i        
        

for s in l:    
    nums = []
    
    for num in s.split(" "):
        nums.append(int(num))

    #print(nums)
    i = 0    
    while i < len(nums):
        c, k = count_consecutive(nums, i)
        print(c, nums[i], end=" ")
        i = k 
        
    
    print()
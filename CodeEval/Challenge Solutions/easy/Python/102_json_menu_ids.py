import sys
import json

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
    m = json.loads(s)
    result = []
    for item_dict in m["menu"]["items"]:
        if item_dict == None:
            continue
        # print(item_dict)
        if "id" in item_dict and "label" in item_dict:
            result.append(int(item_dict["id"]))
    print(sum(result))
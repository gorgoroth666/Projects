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



morse_code = {'A': '.-',     'B': '-...',   'C': '-.-.', 
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',
            
            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.' 
        }


inverse_morse_code = {}


for k, v in morse_code.items():
    inverse_morse_code[v] = k
        

for s in l:
    words = s.split("  ")
    
    for w in words:
        letters = w.split(" ")
        for letter in letters:
            print(inverse_morse_code[letter], end="")
        print(" ", end="")
        
    print()
    
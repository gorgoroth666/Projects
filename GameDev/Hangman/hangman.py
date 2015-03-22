import random

def pick_word(a, b):
    """ 
    Picks a word from a file.
    Makes sure the length of the word is between a and b inclusive.
    """
     
    word_file = open("10000.words.txt", 'r')
    word_list = []
    for line in word_file:
        line = line.strip("\n")
        word_list.append(line)
    word_file.close()
    
    while True:
        w = random.choice(word_list)
        if len(w) <= b and len(w) >= a:
            break
    return w
    
       
secretWord = pick_word(5, 10)

isWon = False
nFailTries = 0

remaining = set(secretWord.lower())

while not isWon:
    
    for c in secretWord:
        if c in remaining:
            print("_", end="")
        else:
            print(c, end="")
    print("")

    while True:
        letter = input("Choose a letter: ")[0].lower()
        if letter.isalpha():
            break
    
    if letter in remaining:       
        remaining.remove(letter)
        if len(remaining) == 0:
            print("Congratulations, you discovered", secretWord, "with only", nFailTries, "fails")
            isWon = True
            break
                
        continue        
        
    nFailTries += 1   
    if nFailTries >= 9:
        print("Game is lost")
        break
import random

words = ["banana", "architect", "soviet"]

secretWord = words[random.randint(0, 2)]
isWon = False
nFailTries = 0
# two sets:
# discovered and remaining
remaining = set(secretWord)
discovered = set()


while not isWon:
    
    for c in secretWord:
        if c in remaining:
            print("_", end="")
        else:
            print(c, end="")
    print("")
        
    letter = input("Choose a letter")[0]
    
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
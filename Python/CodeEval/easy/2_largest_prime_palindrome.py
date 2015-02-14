import math


def isPalindrome(s):
    """
    Takes a string and returns True if it is a palindrome
    """
    return s == s[::-1]






def isPrime(p):
    if p <= 1:
        return False
    if p == 2:
        return True        
    if p % 2 == 0:
        return False
        
    for k in range(3, int(p**0.5) + 1, 2):
        if p % k == 0:
            return False

    return True    
    
    
    
for i in range(1000, 0, -1):
    if isPrime(i) and isPalindrome(str(i)):
        print(i)
        break
def isPalindrome(x: int) -> bool:
    reverseNumber = int(str(x)[::-1])
    if(reverseNumber == x):
        return True
    return False

print(isPalindrome(123))
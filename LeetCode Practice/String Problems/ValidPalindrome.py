import re
# https://leetcode.com/problems/valid-palindrome/
"""
    Pretty simple problem, use 2 pointer technique to check if left and right characters of the string are equal to check
    if it is a palindrome, if not return False. 

    Used a library to get rid of any non-alphanumeric characters from string (!, ., #, $, etc.)
    My solution is O(n) space and time complexity. Probably since I manipulated the string and removed characters to create a new 
    string

    But with the optimal solution instead of manipulating the string you can just ignore any non-alphanumeric character
    and continue to move pointers.

    Optimal Solution:  O(1) space complexity O(n) time complexity
    def isValidPalindrome(s):
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
    

    My Solution:
"""
def validPalindrome(s):

    cleaned_string = re.sub(r'[^a-z0-9]', '', s.lower())

    l, r = 0, len(cleaned_string) - 1

    while l < r:
        if cleaned_string[l] != cleaned_string[r]:
            return False
        
        l += 1
        r -= 1

    print(cleaned_string)
    return True


s = "A man, a plan, a canal: Panama"
print(validPalindrome(s))
print(validPalindrome("0P"))
print(validPalindrome(" "))
# https://leetcode.com/problems/palindrome-number/description/
def palindromeNumber(x):
     

    if x < 0:
       return False
    
    arr = [int(digit) for digit in str(x)]
    print(arr)

    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    
    return True

print(palindromeNumber(10))

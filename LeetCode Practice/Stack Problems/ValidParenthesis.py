# https://leetcode.com/problems/valid-parentheses/
def validParenthessis(s):

    """
    For this problem my first approach was adding all the characters in a stack and checking to see if the 

    """

    stack = []
    dict = {"}" : "{",")" : "(","]" : "["}

    for char in s:
        if char in dict:
            top_element = stack.pop() if stack else '#'
            if dict[char] != top_element:
                print(stack)
                return False
        else:
            stack.append(char)
            
    if stack:
        return False

    return True
            



print(validParenthessis("()"))
print(validParenthessis("()[]{}"))
print(validParenthessis("(}"))
print(validParenthessis("hello"))
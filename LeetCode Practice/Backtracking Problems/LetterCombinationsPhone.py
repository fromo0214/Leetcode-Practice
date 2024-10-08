# https://leetcode.com/problems/letter-combinations-of-a-phone-number/editorial/
def letterCombinationsPhone(digits):
    res = []
    letter_mapping ={"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs",
        "8" : "tuv", "9" : "wxyz"}
    
    def dfs(i, curr):
        if len(digits) == len(curr):
            res.append("".join(curr))
            return
        possible_letters = letter_mapping[digits[i]]
        for letter in possible_letters:
            curr.append(letter)
            dfs(i + 1, curr)
            curr.pop()

    dfs(0, [])
    return res

print(letterCombinationsPhone("23"))
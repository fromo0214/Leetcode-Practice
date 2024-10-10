def phoneLetterCombination(digits):

    phone_letter_map = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs",
        "8" : "tuv", "9" : "wxyz"}
    res = []

    def dfs(i, curr):
        if len(curr) == len(digits):
            res.append("".join(curr))
            return
        
        possible_letters = phone_letter_map[digits[i]]

        for letter in possible_letters:
            curr.append(letter)
            dfs(i + 1, curr)
            curr.pop()

        
    dfs(0, [])
    return res


print(phoneLetterCombination("23"))
        
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
def longestSubstring(s):

    l = 0
    max_len=0
    sett = set()
    for r in range(len(s)):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1
        sett.add(s[r])
        max_len = max(max_len, len(sett))

    return max_len



s = "abcabcbb"
print(longestSubstring(s))
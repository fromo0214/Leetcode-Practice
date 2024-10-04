# https://leetcode.com/problems/longest-repeating-character-replacement/
"""
For this problem I need to check every character in the string and look for
possible insertions where I can replace a character with any letter in the alphabet to
from a substring with the same character.

Example:
s1 = "ABCBA", k1 = 1
output = 3, replace C with B to get "BBB"

s2 = "AALBCD", k2 = 2
output = 4, replace L,B with A to get, "AAAA"

Intuitive Steps:
1. Iterate through the list and keep count of the longest current substring without any changes.
Once 


"""
from collections import defaultdict


def characterReplacement(s, k):
    char_count = {}
    max_len = 0
    max_freq = 0
    l = 0
    for r in range(len(s)):
        char_count[s[r]] = char_count.get(s[r], 0) + 1
        max_freq = max(max_freq, char_count[s[r]])
        #Step 4: Check if the number of replacements exceeds k 
        if (r - l + 1) - max_freq > k:
            char_count[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len

    


print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
print(characterReplacement("AAAA", 2))
print(characterReplacement("ABCABCABC", 1))


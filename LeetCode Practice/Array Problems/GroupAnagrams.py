# https://leetcode.com/problems/group-anagrams/submissions/1388056131/
# https://www.youtube.com/watch?v=vzdNOK2oB2E&ab_channel=NeetCode
#  Time: O(n * m)
from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    if strs == [""]:
        return [[""]]       

    # create a default dictionary to have the values as a list as default
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26 # 26 zeroes in the array, a...z

        for c in s:
            count[ord(c) - ord("a")] += 1 #counting how many of each character we have 

        #lists cannot be keys so you use tuple()
        res[tuple(count)].append(s) #groups all anagrams with this count 

    return res.values()


strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
print(groupAnagrams(strs))
print(groupAnagrams(strs2))
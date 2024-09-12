# https://leetcode.com/problems/longest-consecutive-sequence/
def longestConsecutiveSubSequence(nums):

    sett = set()

    l, r = 0, 0
    
    while r != len(nums):
        if nums[r] + 1 == nums[r + 1]:
            sett.add(nums[r])


nums=[100, 4, 200, ]
    
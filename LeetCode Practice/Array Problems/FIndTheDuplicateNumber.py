# https://leetcode.com/problems/find-the-duplicate-number/description/

def findDuplicateNumber(nums):
    """
    Given an array find the duplicate number in the array where there can only be one repeated number, and if found
    return the number that is repeated.

    Have to solve it only using constant extra space which I was able to do.

    Although at the bottom it is asking if we can solve it using O(n) time complexity.

    Since in my solution I sorted the array the time complexity is O(n log n).
    """


    nums.sort()

    l, r = 0, len(nums) - 1

    while l < r:
        if nums[l] == nums[l + 1]:
            return nums[l]
        else:
            l += 1
        if nums[r] == nums[r - 1]:
            return nums[r]
        else:
            r -= 1
    return 0


print(findDuplicateNumber([3,5,7,2,1,9,9]))
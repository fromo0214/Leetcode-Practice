# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def twoSum(nums, target):

    """
    Have to use constant extra space so O(1), cannot create any data structures to store extra memory.
    O(n) Time Complexity since we iterate through the array

    This is my solution but since I check to see if the difference is in the array then the runtime
    increases and might not be optimal but it is still O(n) time which is the best it can be.


    A better solution would be this: (102 ms run time)
    def twoSum(nums, target):
        
        l, r = 0, len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]

            if total == target:
                return [l + 1, r + 1]
            elif total > target:
                r- = 1
            else:
                l += 1

    My Solution: (5585 ms run time)
    """

    if not nums:
        return []

    l, r = 0, len(nums) - 1

    while l < r:
        difference = target - nums[l]

        # I can remove the condition to check if the difference is in nums and just use elif and else to iterate through array
        # this improves the time complexity to (117 ms run time) which is much better 
        # if difference in nums:
        if (nums[l] == difference or nums[r] == difference) and nums[r] + nums[l] == target:
            return [l + 1, r + 1]
        elif difference < nums[r]:
            r -= 1            
        else:
            l += 1
       
    return [] 


nums = [2, 7, 11, 15]
num2 = [2, 3, 4]

target = 9
target2 = 6
print(twoSum(nums, target))
print(twoSum(num2, target2))
print(twoSum([5, 25, 75], 100))
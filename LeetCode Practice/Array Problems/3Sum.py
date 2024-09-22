# https://leetcode.com/problems/3sum/
from collections import defaultdict


def threeSum(nums):
    """
    For this problem some of the troubles I had were the edge cases of having distinct elements in the triplets. 
    Having an input of [0,0,0,0] i wasn't sure how to handle this since my code 

    """

    nums.sort()
    dict = defaultdict(list)
    count = 0
    
    for i in range(len(nums)):
        # in case of having repeated elements like [0,0,...] or [1,1,...] after the first iteration we skip it
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]

            # if the sum is greater than 0 we decrease the sum by decreasing the right pointer since the
            # array is sorted
            if three_sum > 0:
                r -= 1
            # if the sum is less than 0 than we increase the sum by increasing the left pointer since the
            # array is sorted 
            elif three_sum < 0:
                l += 1
            else:
                # could also do this if i didnt wanna use a dictionary 
                # list.append([nums[i],...])
                dict[count].append(nums[i])
                dict[count].append(nums[l])
                dict[count].append(nums[r])
                count += 1
                # originally i incremented and made the key i
                # i += 1
                # but since i was incrementing the i in the for loop it wasnt collecting the elements correctly

                # [-2,-2,0,2,2]
                # for cases like this, where there are elements next to each other that are duplicates
                # so we just increment the left pointer 
                while l < r and nums[l] == nums[l + 1]:
                    l += 1

                l += 1
                r -= 1           

    return dict.values()


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
print(threeSum([0,0,0,0]))
print(threeSum([1,-1,-1,0]))
print(threeSum([-2, 0, 1, 1, 2]))
print(threeSum([-2,-2,0,2,2]))


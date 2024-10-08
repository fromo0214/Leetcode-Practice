# https://leetcode.com/problems/subsets-ii/
"""
For my solution it is not fully optimized since I have a condition that checks if
the subset is not in the result list which takes O(k) time. 

In the worse case my solution can have a O(2^n * n * k) time complexity, due to the
duplication check.

This is the optimized solution

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def dfs(i):
            res.append(subset.copy())            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                dfs(j + 1)
                subset.pop()
    

        dfs(0)

        return res


"""

def subsetsWithDup(nums):
    res = []
    subset = []
    nums.sort()
    def dfs(i):
        if subset not in res:
            res.append(subset.copy())
        
        if i >= len(nums):
            return
    
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res

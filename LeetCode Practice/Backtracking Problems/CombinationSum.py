# https://leetcode.com/problems/combination-sum/

def combinationSum(nums, target):

    res = []
    # Current array that is going to hold integers that add up to target.
    # Conduct recursive dfs to get decision tree and get every possible
    # combination we can get to add up to the target.
    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        
        if i >= len(nums) or total > target:
            return
        
        curr.append(nums[i])
         # Here we leave the index the same since we are allowed
            # to reuse elements unlimited times
        dfs(i, curr, total + nums[i])

        curr.pop()
        # next decision is where we cant include this candidate,
        # clean up a little bit
        dfs(i + 1, curr, total)


    dfs(0, [], 0)
    return res

print(combinationSum([1,2,3], 3))


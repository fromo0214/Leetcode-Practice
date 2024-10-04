# https://leetcode.com/problems/subsets/description/
def subsets(nums):
    if not nums:
        return []
    res = []

    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # decision to NOT include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return res

     
    

print(subsets([1,2,3]))
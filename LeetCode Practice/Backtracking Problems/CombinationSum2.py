# https://leetcode.com/problems/combination-sum-ii/description/
def combinationSum2(nums, target):
    n = len(nums)
    res = []
    nums.sort()
    def dfs(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        
        if total > target or i >= n:
            return
        
        curr.append(nums[i])
        dfs(i + 1, curr, total + nums[i])
        curr.pop()

        while i + 1 < n and nums[i] == nums[i + 1]:
            i +=1

        dfs(i + 1, curr, total)

    dfs(0, [], 0)
    return res

print(combinationSum2([1,2,3], 3))


def practice(candidates, target):

    res = []
    n = len(candidates)
    candidates.sort()
    def dfs(i, curr, total):

        if total == target:
            res.append(curr.copy())
            return
        if i >= n or total > target:
            return

        curr.append(candidates[i])
        dfs(i + 1, curr, total + candidates[i])
        curr.pop()
        
        while i + 1 < n and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, cuurr, total)

    dfs(0, [], 0)

    return res
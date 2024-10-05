# https://leetcode.com/problems/subsets/description/
def subsets(nums):
    if not nums:
        return []
    res = []
    
    subset = []
    def dfs(i):
        # If this condition happens then we know we are passed the leaf node
        # of the decision tree, so add the subset to the result 
        if i >= len(nums):
            res.append(subset.copy())
            return
        # decision to include nums[i], left branch of decision tree
        subset.append(nums[i])
        dfs(i + 1)

        # decision to NOT include nums[i], right branch of decision tree
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return res

     
    

print(subsets([1,2,3]))
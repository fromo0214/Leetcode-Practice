# https://leetcode.com/problems/permutations/description/
def permute(nums):
  # Initialize the result list to store all permutations
        res = []

        # Define a helper function dfs to explore permutations using Depth-First Search
        def dfs(curr):
            # Base case: If the current permutation has the same length as the input list
            if len(curr) == len(nums):
                # Add a copy of the current permutation to the result list
                res.append(curr.copy())
                return
            
            # Iterate through each number in the input list
            for i in range(len(nums)):
                # If the number is already in the current permutation, skip it
                if nums[i] in curr:
                    continue
                # Add the current number to the permutation
                curr.append(nums[i])
                # Recursively call dfs to build the next permutation
                dfs(curr)
                # Backtrack by removing the last added number, exploring other possibilities
                curr.pop()
        
        # Start the DFS with an empty list to begin building permutations
        dfs([])

        # Return the list of all permutations generated
        return res

print(permute([1,2,3]))
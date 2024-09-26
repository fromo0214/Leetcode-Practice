# https://leetcode.com/problems/invert-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Recursive dfs to solve and just swap the children
Runtime and Space Complexity: O(n)
"""
def invertTree(root):

    if not root:
        return None
    
    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)

    return root

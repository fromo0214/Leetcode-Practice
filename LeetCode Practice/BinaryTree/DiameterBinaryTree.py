class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def diameterOfBinaryTree(root):
    # create a global variable
    diameter = 0
   
    def dfs(root):
        if not root:
            return 0

        left_count = dfs(root.left)
        right_count = dfs(root.right)  
        diameter = max(diameter, left_count + right_count)
        return max(left_count, right_count) + 1

    
    dfs(root)

    return diameter




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(diameterOfBinaryTree(root))



# https://leetcode.com/problems/balanced-binary-tree/description/
class TreeNode(object):
    """
    My intuition when solving this problem is correct but the only reason why I couldn't get the solution
    was because I had to call the recursive function of isBalanced to traverse the left and right subtrees at thr end. 
    Ultimately hitting one of the base cases
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    if not root:
        return True
    
    leftCount = DFS(root.left)
    rightCount = DFS(root.right)

    if abs(leftCount-rightCount) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)


def DFS(root):
    if not root:
        return 0
    
    left_depth = DFS(root.left)
    right_depth = DFS(root.right)

    return max(left_depth, right_depth) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(isBalanced(root))


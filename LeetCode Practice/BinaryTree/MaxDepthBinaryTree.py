# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
def maxDepth(root):
    if not root:
        return 0
    
    leftCount = maxDepth(root.left) + 1
    rightCount = maxDepth(root.right) + 1

    return max(leftCount, rightCount)

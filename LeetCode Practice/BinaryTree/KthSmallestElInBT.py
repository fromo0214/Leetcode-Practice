# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def kthSmallestElement(root, k):

    if not root:
        return 
    
    def in_order_traversal(node):
        lst = []

        if node:
            lst = in_order_traversal(node.left)
            lst.append(node.val)
            lst = lst + in_order_traversal(node.right)
        
        return lst
    
    res = in_order_traversal(root)
    print(res)
    return res[k - 1] 
    



root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
print(kthSmallestElement(root, 1))
#  Definition for a binary tree node.
import collections


class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
def minDepth(root):

    if not root:
        return 0
    left = minDepth(root.left)
    right = minDepth(root.right)
    
    if root.left is None and root.right is None:
        return 1
    
    if root.left is None:
        return 1 + right
    if root.right is None:
        return 1 + left
    
    return min(left, right) + 1
        


    #     1
    #  /     \
    # 3       2
    #   \
    #     5

     


# https://leetcode.com/problems/subtree-of-another-tree/description/

def sameTree(p, q):
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return (sameTree(p.left, q.left) and sameTree(p.right, q.right))
        return False

def isSubtree(root, subRoot):
    """
    :type root: TreeNode
    :type subRoot: TreeNode
    :rtype: bool
    """
    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# https://leetcode.com/problems/invert-binary-tree/

def invertTree(root):
    
       """
       :type root: TreeNode
       :rtype: TreeNode
       """
       if not root:
           return None
       
       root.left, root.right = root.right, root.left
       invertTree(root.right)
       invertTree(root.left)
       return root



# https://leetcode.com/problems/find-leaves-of-binary-tree/description/
def find_leaves_binary_tree(root):

     
    dict = collections.defaultdict(list)

    def postorder_traversal(node, layer):

        if not node:
            return layer
        # [1,2,3,4,5]
        
        left = postorder_traversal(node.left, layer)
        right = postorder_traversal(node.right, layer)

        layer = max(left, right)

        dict[layer].append(node.val)

        return layer + 1
    
    postorder_traversal(root, 0)
    

    return dict.values()
    
       

root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(find_leaves_binary_tree(root))
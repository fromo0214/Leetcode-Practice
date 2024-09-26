# https://leetcode.com/problems/subtree-of-another-tree/
"""
For this problem I was making the mistake of traversing the subRoot's children when I would do a 
recursive call for the isSubTree function but we are not supposed to do that because we traverse the subroot
when we call the sametree function
"""
def isSubTree(root, subRoot):
    if not subRoot:
        return True

    if not root:
        return False
    
    if sameTree(root, subRoot):
        return True
    
    return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)

def sameTree(p, q):
    if not p and not q:
        return True
    
    if p and q and p.val == q.val:
        return (sameTree(p.left, q.left) and sameTree(p.right, q.right))
    
    return False
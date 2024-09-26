# https://leetcode.com/problems/same-tree/
def sameTree(p, q):
    if not p and not q:
        return True
    elif p is None:
        return False
    elif q is None:
        return False

    if p and q:
        if p.val != q.val:
            return False
        return sameTree(p.left, q.left) and sameTree(p.right, q.right) 

    return True 
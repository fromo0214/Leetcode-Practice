def isValidBST(root):
    if not root:
        return True
    def dfs(root):
        if not root:
            return True
        val = root.val
        if root.left:
            left_val = root.left.val
        else:
            left_val = 0
        if root.right:
            right_val = root.right.val
        else:
            right_val = 0
        
        if left_val < val and right_val > val:
            return True
        
        return dfs(root)
            
        
    return isValidBST(root.left) and isValidBST(root.right)


       
        
        
def isValidBST(root):

    if not root:
        return True
    # left and right variables define boundaries

    def valid(node, left, right):

        if not root:
            return True
       
        if not node.val < right and node.val > left:
            return False
        
        return valid((node.left, left, node.val) and valid(node.right, node.val, right))
    
    return valid(root, float("-inf"), float("inf"))
          



def validBST(root):
    if not root:
        return True

    def validate(node, left, right):
        if not node:
            return True
        
        if node.val <= left or node.val >= right:
            return False
        

        return validate(node.left, left, node.val) and validate(node.right, node.val, right)


        


       
    return validate(root, float("-inf"), float("inf"))
        
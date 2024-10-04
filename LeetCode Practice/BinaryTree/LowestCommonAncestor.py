class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def lowest_common_ancestor(root, p, q):
    if not root:
         return

    def in_order_traversal(node):
            lst = []
            if node:
                lst = in_order_traversal(node.left)
                lst.append(node.val)
                lst = lst + in_order_traversal(node.right)

            return lst
    
    lst = in_order_traversal(root)

from collections import deque

# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def levelOrderTraversal(root):
    if not root: 
         return []
    
    lst = []  
    queue = deque([root])

    # Add the root to the queue
    # While the queue is not empty:
    while queue:
      level_size = len(queue)
      level = []
      for i in range(level_size):
        #Pop the next node off the queue (pop from the left side!
        node = queue.popleft()
        if node:
            level.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    #   Add the popped node to the list of explored nodes
    #   Add each of the popped node's children to the end of the queue
      if level:
        lst.append(level)
        
    # Return the list of visited nodes
    
    return lst
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrderTraversal(root))
          



from collections import deque


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def search(root, target):
  if root:
    print(f"Checking node with value: {root.val}")
  else:
    print("Reached a None node")

  if root is None or root.val == target:
    if root:
      print(f"Found node with value: {root.val}")
    else:
      print(f"Value {target} not found in the tree.")
    return root

  if target < root.val:
    print(f"Going left from node with value: {root.val}")
    return search(root.left, target)

  print(f"Going right from node with value: {root.val}")
  return search(root.right, target)





def inorderTraversal(root):
  result = []

  if root:
    print(f"Traversing left subtree of node with value {root.val}")
    result = inorderTraversal(root.left)

    print(f"Visiting node with value {root.val}")
    result.append(root.val)

    print(f"Traversing right subtree of node with value {root.val}")
    result = result + inorderTraversal(root.right)

  return result

def preorderTraversal(root):
  result = []

  if root:
    print(f"Visiting node with value {root.val}")
    result.append(root.val)

    print(f"Traversing left subtree of node with value {root.val}")
    result = result + preorderTraversal(root.left)

    print(f"Traversing right subtree of node with value {root.val}")
    result = result + preorderTraversal(root.right)

  return result

# root = TreeNode(50)
# root.left = TreeNode(30)
# root.right = TreeNode(70)
# root.left.left = TreeNode(20)
# root.left.right = TreeNode(40)
# root.right.left = TreeNode(60)
# root.right.right = TreeNode(80)


def level_order(root):
  # If the tree is empty:
  # return an empty list
  if not root:
    return []
  # Create an empty queue using deque
  # Create an empty list to store the explored nodes
  queue = deque()
  lst = []


  # Add the root to the queue
  queue.append(root)
  # While the queue is not empty:
  while queue:
    new_lst = []
    node = queue[0]
    queue.popleft()
    #print(node.val)
    new_lst.append(node.val)
    lst.append(new_lst)

    
  # Pop the next node off the queue (pop from the left side!)
  # Add the popped node to the list of explored nodes

  # Add each of the popped node's children to the end of the queue
    if node.left:
      queue.append(node.left)
      new_lst.append(node.val)
    if node.right:
      queue.append(node.right)
      new_lst.append(node.val)


  # Return the list of visited nodes
  return lst

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(level_order(root))
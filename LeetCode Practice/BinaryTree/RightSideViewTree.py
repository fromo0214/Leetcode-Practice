# https://leetcode.com/problems/binary-tree-right-side-view/
"""
Input:
Given a binary tree:
Output:
Any node that is seen from the right side for each level gets appended to a list.

tree = [1, 2]
output = [1, 2]

Intuition Steps:
1. Start at root which if not null, add it to list because it will always be able to be seen from the right side.
2. Conduct level order traversal or BFS, If a right child does not exist, and if there is a left child, we will be able to
see it from the right side since there is not a node in the way and add that node to the list.
3. Once the level order traversal or BFS is done, we obtain a list with all of the nodes in each level.
4.If the length of the list is greater than or equal to 2 then we must return the list node in the list 


"""
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def right_side_view_binary_tree(root):

    if not root:
        return None


    lsts = []    
    
    queue = deque([root])

    while queue:
        level_size = len(queue)
        new_lst = []
        for i in range(level_size):
            node = queue.popleft()
            new_lst.append(node.val)    
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        lsts.append(new_lst)
    
    res = []
    for lst in lsts:
        if len(lst) >= 2:
            res.append(lst[-1])
        else:
            res.append(lst[0])

    
    return res

# Sample input and output
#           1 <-
#          /
#         2   <-

root = TreeNode(1)
root.left = TreeNode(2)
print(right_side_view_binary_tree(root)) #Output = [1, 2]

# Sample input and output
#           1 <-
#          / \
#         2   3 <-
#          \   \
#           5   4 <-

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(4)
print(right_side_view_binary_tree(root2)) #Output = [1, 3, 4]


def practice(root):

    if not root:
        return 
    
    def level_order_traversal(root):
        if not root:
            return None
        lst = []
        queue = deque([root])

        while queue:
            new_lst = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                new_lst.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            lst.append(new_lst)

    lsts = level_order_traversal(root)
    res = []
    for lst in lsts:
        res.append(lst[-1])

    return res




def practice(root, k):
    if not root:
        return
    
    def in_order_traversal(root):
        lst = []
        if root:
            lst = in_order_traversal(root.left)
            lst.append(root.val)
            lst = lst + in_order_traversal(root.right)

        return lst
    
    lst = in_order_traversal(root)

    return lst[k - 1]
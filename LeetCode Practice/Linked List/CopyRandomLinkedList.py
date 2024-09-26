# https://leetcode.com/problems/copy-list-with-random-pointer/
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    
    
    oldToCopy = {None : None}
    curr = head

    while curr:
        copy = Node(curr.val)
        oldToCopy[curr] = copy 
        curr = curr.next

    print(oldToCopy)
    curr = head

    while curr:
        copy = oldToCopy[curr]  
        # if the next node is null, we set it to none which is why we initialized it in the hashmap
        copy.next = oldToCopy[curr.next]
        # if
        copy.random = oldToCopy[curr.random]

        curr = curr.next

    return oldToCopy[head]

head = Node(0, 1)
head.random = head
head.next = Node(1, 0)
print(copyRandomList(head))
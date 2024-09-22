# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    
    if not head:
        return None

    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr  
        curr = temp

    lst = []

    while prev:
        lst.append(prev.val)
        prev = prev.next

    print(lst)
    return prev


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reverseLinkedList(head)
        
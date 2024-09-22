# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthNodeFromLinkedList(head, n):
    lst = []
    lst_head = head
    while lst_head:
        lst.append(lst_head)
        lst_head = lst_head.next

    index = len(lst) - n

    dummy = ListNode(0)
    dummy.next = head
    if index == 0:
        return head.next

    lst[index - 1].next = lst[index].next

    return dummy.next






head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2
print(removeNthNodeFromLinkedList(head, n))











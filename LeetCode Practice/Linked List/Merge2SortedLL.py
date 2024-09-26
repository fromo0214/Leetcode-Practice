# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    curr1 = list1
    curr2 = list2

    dummy = ListNode()
    curr = dummy

    while curr1 and curr2:
        if curr1.val > curr2.val:
            curr.next = curr2
            curr2 = curr.next
        else:
            curr.next = curr1
            curr1 = curr1.next
        
        curr = curr.next 

    if curr1:
        curr.next = curr1
    else:
        curr.next = curr2
       
    return dummy.next

            

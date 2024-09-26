# https://leetcode.com/problems/merge-k-sorted-lists/
"""
Given an array of linked lists, return all the nodes sorted into
1 linked list

array = [[1,2,3],[1,2,3]]
output = [1,1,2,2,3,3]
"""
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.merge_sorted_list(l1,l2))
            lists = temp

        return lists[0]


    def merge_sorted_list(self, l1, l2):

        dummy = ListNode()
        curr = dummy

        while l1 and l2:

            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next

            curr = curr.next

        if l1:
            curr.next = l1
        else:
            curr.next = l2
            
        
        return dummy.next
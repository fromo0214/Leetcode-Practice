class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def MergeKSortedList(lists):

    values = []

    for nums in lists:
        for num in nums:
            values.append(num)

    values.sort()

    dummy = ListNode()
    head = dummy

    for i in range(len(values)):
        head = ListNode(values[i])
        head = head.next
    
    return dummy.next


MergeKSortedList([[1,2,3],[1,2,3]])

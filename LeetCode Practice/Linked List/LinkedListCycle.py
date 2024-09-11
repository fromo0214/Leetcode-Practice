class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if not head:
        return False
    
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

head = ListNode(3)
head.next = ListNode(3)




print(hasCycle(head))

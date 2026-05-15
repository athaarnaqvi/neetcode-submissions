# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        while  fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        current = l2
        prev = None
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        l2 = prev

        output = ListNode()
        current = output

        while l1 and l2:
            current.next = l1
            l1 = l1.next

            current = current.next

            current.next = l2
            l2 = l2.next

            current = current.next
        
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        head = output.next





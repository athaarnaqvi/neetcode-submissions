# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        if head is None:
            return False
        for i in range (50):
            current = current.next
            if current is None:
                return False
        
        return True
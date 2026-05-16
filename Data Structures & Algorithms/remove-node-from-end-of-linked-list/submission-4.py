# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return head.next
        
        current = head
        next = None
        prev = None
        count = 0
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count +=1
       
        head = prev
        prev = None

        current = head
        if n == 1:
            current = current.next
            head = current
        elif count == n:
            current = head

            while current.next.next is not None:
                current = current.next

            current.next = None
            

        else:
        
            for i in range (n-1):
            
                prev = current
                current = current.next
            
            
            prev.next = current.next

        current = head
        prev = None
        next = None
        
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        head = prev

        return head
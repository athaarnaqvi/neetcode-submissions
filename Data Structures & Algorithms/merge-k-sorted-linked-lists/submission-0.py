# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        if len(lists) == 0 or lists is None:
            return None
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            output = ListNode()
            current = output

            while list1 is not None and list2 is not None:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
        

            if list2 is not None:
                current.next = list2
            elif list1 is not None:
                current.next = list1
                
            return output.next
        
        for i in range(1, len(lists)):
            result = mergeTwoLists(self,list1=lists[i], list2=lists[i - 1])
            lists[i] = result
        
        return lists[len(lists)-1]


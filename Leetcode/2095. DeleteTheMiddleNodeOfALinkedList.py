# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional:
    def __init__(self, val=None):
        self.val = val

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        dummy = ListNode(-1)
        dummy.next = head
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        prev_idx = length // 2
        
        temp = dummy
        i = 0
        while i < prev_idx:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        return dummy.next
            
        

            
            
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional:
    def __init__(self, val=None):
        self.val = val
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        temp = head
        while temp:
            temp = temp.next
            i += 1

        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        for j in range(i - n):
            temp = temp.next
        
        temp.next = temp.next.next if n != 1 else None
        return dummy.next
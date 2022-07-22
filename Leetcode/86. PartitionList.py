# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Optional:
    def __init__(self, val=None):
        self.val = val
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res = ListNode(1000)
        temp = res
        
        temp2 = head
        while temp2:
            if temp2.val < x:
                temp.next = ListNode(temp2.val)
                temp = temp.next
            temp2 = temp2.next
        
        temp2 = head
        while temp2:
            if temp2.val >= x:
                temp.next = ListNode(temp2.val)
                temp = temp.next
            temp2 = temp2.next
                
        return res.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional:
    def __init__(self, val=None):
        self.val = val
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        left -=1
        right -=1
        idx = -1
        temp = ListNode(-1000, head)
        head = temp
        
        while idx < (left - 1):
            idx += 1
            temp = temp.next

        left_prev = temp
        temp = temp.next
        stack = []
        for i in range(left, right+1):
            stack.append(ListNode(temp.val))
            temp = temp.next
            
        right_after = temp
        
        temp2 = left_prev
        for i in range(len(stack)-1,-1,-1):
            temp2.next = stack[i]
            temp2 = temp2.next
        
        temp2.next = right_after
        return head.next
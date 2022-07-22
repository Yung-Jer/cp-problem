# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Optional:
    def __init__(self, val=None):
        self.val = val

# Two running pointers pointing to two heads of the linked lists
# When the pointers pointing to None (i.e. end of the linked list), switch to head of another linked list
# This will make two pointers eventually meet at a common node because they will run the same steps
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = headA
        second = headB
        
        while first != second:
            first = first.next if first != None else headB
            second = second.next if second != None else headA
            
        return first
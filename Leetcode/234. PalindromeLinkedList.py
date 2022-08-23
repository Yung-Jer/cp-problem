# Definition for singly-linked list.

# Answer takes O(n) time complexity and O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional:
    def __init__(self, val=None):
        self.val = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pt1, pt2 = head, head
        
        while pt2.next and pt2.next.next:
            pt1 = pt1.next
            pt2 = pt2.next.next
        
        if pt2.next: # for even nodes case
            pt1 = pt1.next
            pt2 = pt2.next
        
        # reversing the second half of the linked list
        prev = None
        curr = pt1
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        pt1 = head
        
        while pt2:
            if pt1.val != pt2.val:
                return False
            pt1, pt2 = pt1.next, pt2.next
        return True
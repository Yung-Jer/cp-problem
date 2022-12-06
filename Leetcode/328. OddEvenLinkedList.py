# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        total = 1
        curr = head
        if not curr:
            return curr

        while curr.next:
            curr = curr.next
            total += 1
        
        tail = curr
        curr = head
        prev = ListNode('#', head)

        for i in range(total):
            if cnt % 2 == 1:
                tail.next = ListNode(curr.val)
                tail = tail.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
            cnt += 1
        return head
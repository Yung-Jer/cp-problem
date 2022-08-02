import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional:
    def __init__(self, val=None):
        self.val = val

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ele in lists:
            while ele:
                heapq.heappush(heap, ele.val)
                ele = ele.next
                
        head = ListNode(0)
        temp = head
        
        while heap:
            temp.next = ListNode(heapq.heappop(heap))
            temp = temp.next
            
        return head.next
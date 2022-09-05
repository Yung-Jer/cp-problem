
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while q:
            temp = []
            for i in range(len(q)):
                cur = q.popleft()
                temp.append(cur.val)
                for j in cur.children:
                    q.append(j)
            ans.append(temp)
            
        return ans
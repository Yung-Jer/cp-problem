# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Optional:
    def __init__(self, val):
        self.val = val=None

import collections        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        q = collections.deque()
        q.append(root)
        ans = []
        
        while q:
            _sum = 0
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                _sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(_sum / n)
        return ans
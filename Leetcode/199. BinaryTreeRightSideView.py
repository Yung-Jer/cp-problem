# Definition for a binary tree node.
import collections

class Optional:
    def __init__(self, val):
        self.val = val
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            num = len(q)
            for i in range(num):
                node = q.popleft()
                val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
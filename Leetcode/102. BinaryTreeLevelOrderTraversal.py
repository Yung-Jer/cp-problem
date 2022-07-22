import collections
# Definition for a binary tree node.
class Optional:
    def __init__(self, val=None):
        self.val = val
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        q = collections.deque()
        res = []
        q.append(root)
        
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
            
        return res
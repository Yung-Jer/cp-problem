# Definition for a binary tree node.
import collections

class Optional:
    def __init__(self, val=None):
        self.val = val
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Method 1: BFS
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

# Method 2: DFS
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        res = []
        
        def dfs(node, level):
            if level >= len(res):
                res.append(node.val)
            else: 
                res[level] = node.val
                
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
                
        dfs(root, 0)
        return res
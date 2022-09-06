# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Optional:
    def __init__(self, val=None):
        self.val = val
        
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 0
            cur = 1 if node.val == 1 else 0
            l = dfs(node.left)
            r = dfs(node.right)
            if l == 0:
                node.left = None
            if r == 0:
                node.right = None
            cur = cur or l or r
            return cur
        
        dfs(root)
        return None if root.val == 0 and not (root.left or root.right) else root
            
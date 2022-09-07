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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return ""
            res = str(node.val)
            if not node.left and node.right:
                res += ("()(" + dfs(node.right) + ")")
            elif node.left and node.right:
                res += ("(" + dfs(node.left) + ")" + "(" + dfs(node.right) + ")")
            elif node.left:
                res += ("(" + dfs(node.left) + ")")
            return res
        return dfs(root)
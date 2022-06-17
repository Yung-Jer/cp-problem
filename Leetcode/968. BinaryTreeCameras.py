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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0
            val = dfs(node.left) + dfs(node.right)
            if val == 0: # This is a leaf
                return 3              
            elif val < 3:
                return 0
            nonlocal res
            res += 1
            return 1
        
        return res+1 if dfs(root) >= 2 else res

# Credit to: https://leetcode.com/karan_8082/
# Refer from: https://leetcode.com/problems/binary-tree-cameras/discuss/2160278/PYTHON-oror-EXPLAINED-oror
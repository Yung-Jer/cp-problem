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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, _sum):
            if node:
                if not (node.left or node.right) and _sum + node.val == targetSum:
                    return True
                elif not (node.left or node.right):
                    return False
                new_sum = _sum + node.val
                res = False
                if node.left:
                    res = res or dfs(node.left, new_sum)
                if node.right:
                    res = res or dfs(node.right, new_sum)
                return res
            return False
        return dfs(root, 0)
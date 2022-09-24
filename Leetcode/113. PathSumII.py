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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        res = []
        def dfs(node, _sum, path):
            if node:
                new_sum = _sum + node.val
                new_path = path.copy()
                new_path.append(node.val)
                if not (node.left or node.right) and new_sum == targetSum:
                    res.append(new_path)
                if node.left:
                    dfs(node.left, new_sum, new_path)
                if node.right:
                    dfs(node.right, new_sum, new_path)
        
        dfs(root, 0, [])
        return res
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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, _set):
            if not node:
                return 0
            if node.val in _set:
                _set.remove(node.val)
            else:
                _set.add(node.val)
            if not (node.left or node.right):
                return 1 if len(_set) <= 1 else 0
            new_set = _set.copy() # must create a new copy otherwise it will be changed in dfs
            left = dfs(node.left, _set)
            right = dfs(node.right, new_set)
            return left + right
        return dfs(root, set())
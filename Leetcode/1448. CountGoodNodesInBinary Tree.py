# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            # max_val is the current largest element from top root to the current node
            cnt = 0
            if node.val >= max_val:
                cnt += 1
                max_val = node.val
            if node.left:
                cnt += dfs(node.left, max_val)
            if node.right:
                cnt += dfs(node.right, max_val)
            return cnt
        
        return dfs(root, root.val)
                    
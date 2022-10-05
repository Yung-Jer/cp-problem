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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        
        def dfs(node, lvl):
            if node:
                if lvl == depth - 1:
                    if node.left:
                        new = TreeNode(val)
                        new.left = node.left
                        node.left = new
                    else:
                        node.left = TreeNode(val)
                    if node.right:
                        new2 = TreeNode(val)
                        new2.right = node.right
                        node.right = new2
                    else:
                        node.right = TreeNode(val)
                    return
                if node.left:
                    dfs(node.left, lvl + 1)
                if node.right:
                    dfs(node.right, lvl + 1)
        dfs(root, 1)
        return root
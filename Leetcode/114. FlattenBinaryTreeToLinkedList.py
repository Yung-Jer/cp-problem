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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if node:
                if node.left:
                    pre = node.left
                    while pre.right:
                        pre = pre.right
                    pre.right = node.right
                    node.right = node.left
                    node.left = None
                traverse(node.right)
                
        traverse(root)
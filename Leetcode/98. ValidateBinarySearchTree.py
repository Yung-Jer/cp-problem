# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Optional:
    def __init__(self, value=None):
        self.value = value
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -10000000000000000
        def inorder(node):
            if node:
                flag = True
                flag = flag and inorder(node.left)
                if node.val <= self.prev:
                    return False
                self.prev = node.val
                flag = flag and inorder(node.right)
                return flag
            return True
        return inorder(root)
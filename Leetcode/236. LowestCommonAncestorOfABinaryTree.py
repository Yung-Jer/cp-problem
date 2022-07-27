# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(node):
            if not node:
                return None
            elif node == p or node == q:
                return node
            else:
                left, right = recur(node.left), recur(node.right)
                if left and right:
                    return node
                else:
                    return left or right
        return recur(root)
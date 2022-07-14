# Definition for a binary tree node.
class Optional:
    def __init__(self, val):
        self.val = val
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        n = len(preorder)
            
        if n:
            idx = 0
            def recur(inorder):
                if inorder:
                    nonlocal idx
                    temp_index = inorder.index(preorder[idx])
                    node = TreeNode(inorder[temp_index])
                    idx += 1
                    node.left = recur(inorder[:temp_index])
                    node.right = recur(inorder[temp_index+1:])
                    return node
            return recur(inorder)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Optional:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        ans = []
        def dfs(node, row, col):
            if node:
                ans.append([node.val, row, col])
                dfs(node.left, row+1, col-1)
                dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        ans.sort(key=lambda x: (x[2], x[1], x[0]))
        d = defaultdict(list)
        for val, r, c in ans:
            d[c].append(val)
        l=[]
        for i in d.values():
            l.append(i)
        return l
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
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]: 
        def recur(arr):
            if arr:
                m = len(arr) // 2
                return TreeNode(val = arr[m], left = recur(arr[:m]), right = recur(arr[m+1:]))
            
        return recur(nums)
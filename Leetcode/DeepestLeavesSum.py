# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Initialize a dictionary with level as key, and sum of all leaves at this level as value
        level_dct = {}

        def recurr(root, level):
            if not (root.left or root.right):
                if level_dct.get(level, 0) == 0:
                    level_dct[level] = root.val
                else:
                    level_dct[level] += root.val
            else:
                if root.left:
                    recurr(root.left, level + 1)
                if root.right:
                    recurr(root.right, level + 1)
        recurr(root, 0)

        # Find the max key in the dictionary
        max_key = max(list(level_dct.keys()))
        return level_dct[max_key]
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        
        while q:
            layerlength = len(q)
            prev = Node(-200)
            
            for i in range(layerlength):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                    prev.next = current.left
                    prev = current.left
                if current.right:
                    q.append(current.right)
                    prev.next = current.right
                    prev = current.right
        return root

# Another Solution: Preorder Traversal (Root -> Left -> Right) + Dictionary/HashMap (Taken from Leetcode forum Author: JSTM2022)
# def connect(self, root: 'Node') -> 'Node':
#     def preOrder(node, depth, dic):
#         if not node:
#             return
#         if depth not in dic:
#             dic[depth] = node
#         else:
#             dic[depth].next = node
#             dic[depth] = node
#         preOrder(node.left, depth + 1, dic)
#         preOrder(node.right, depth + 1, dic)
#     preOrder(root, 1, {})
#     return root
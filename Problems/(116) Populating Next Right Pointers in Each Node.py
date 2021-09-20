# Question Link
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Description
'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition (Down there with the question)



Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect(root):
            if not root: return 
            
            if root.right:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
            connect(root.left)
            connect(root.right)
        connect(root)
        return root 
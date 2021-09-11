# Question Link
# https://leetcode.com/problems/invert-binary-tree/

# Description
'''
Given the root of a binary tree, invert the tree, and return its root.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node == None:
                return 

            node.right,node.left = node.left, node.right
            
            invert(node.left)
            invert(node.right)
            return
        invert(root)
        return root
            
    
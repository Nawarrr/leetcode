# Question Link
# https://leetcode.com/problems/validate-binary-search-tree/

# Description
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorderTraversal(node , list):
            if node == None:
                return list
            inorderTraversal(node.left , list)
            list.append(node.val)
            inorderTraversal(node.right , list)
            return list
        
        list= inorderTraversal(root , [])
        element = float('-inf')
        for i in list:
            if i <= element:
                return False
            else:
                element =i
        return True
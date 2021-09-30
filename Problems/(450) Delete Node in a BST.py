# Question Link
# https://leetcode.com/problems/delete-node-in-a-bst/

# Description
'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

- Search for a node to remove.
- If the node is found, delete the node.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root : return       
        
        if root.val == key:
            if not root.left and not root.right : return None
            if root.left and not root.right : return root.left
            if root.right and not root.left : return root.right
            node = root.right
            while node.left : node = node.left
            root.val = node.val
            root.right = self.deleteNode(root.right,root.val)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            root.left = self.deleteNode(root.left,key)
            
        return root
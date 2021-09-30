# Question Link
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Description
'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root,output):
            if not root: return
            
            inorderTraversal(root.left, output)
            output.append(root.val)
            inorderTraversal(root.right, output)
            return output
        
        return inorderTraversal(root, [])[k-1]
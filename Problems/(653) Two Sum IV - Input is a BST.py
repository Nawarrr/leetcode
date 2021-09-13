# Question Link
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Description 
'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def inorderTraversal(node , hash , k):
            if node == None:
                return False
            if hash.get(k-node.val):
                return True
            else:
    
                hash[node.val] = True
            return inorderTraversal(node.left , hash , k) or inorderTraversal(node.right , hash , k )
            

                
        return inorderTraversal(root, {}, k)
            
# Question Link
# https://leetcode.com/problems/path-sum/

# Description
'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, sum):
            if node == None:
                return 
            if node.right == None and node.left == None:
                return node.val == sum
            
                
            return dfs(node.right ,  sum- node.val ) or dfs(node.left , sum - node.val)
            
            
            
            
        return dfs(root , targetSum)
# Question Link
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Description
'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def insert(array):
            
            l = 0
            r = len(array)
            mid = (l+r)//2
            if r <= l:
                return 
            root = TreeNode(array[mid])
            root.left = insert(array[l:mid])
            root.right = insert(array[mid+1:r])
            return root
        
        return insert(nums)
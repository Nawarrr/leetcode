# Question Link
# https://leetcode.com/problems/symmetric-tree/

# Description
'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ----------------------------------- Recursive Soultion -------------------------------- #
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(t1 , t2):
            if t1 == None and t2 == None: 
                return True
            if t1 == None or t2 ==None: 

                return False
            
            return (t1.val == t2.val) and isMirror(t1.left , t2.right) and isMirror(t1.right , t2.left)
        
        return isMirror(root,root)
    # ----------------------------------- Iteritave Soultion -------------------------------- #
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        queue = []
        if  root.right == None and root.left == None :
            return True
        queue.append(root)
        queue.append(root)
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if left.val != right.val:
                return False
            
            if left.left and right.right:
                queue.append(left.left)
                queue.append(right.right)
            elif left.left or right.right:
                return False
            
            if left.right and right.left:
                queue.append(left.right)
                queue.append(right.left)
            elif left.right or right.left:
                return False
            
        return True
        
        
                
            
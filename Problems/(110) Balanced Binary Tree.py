# Question Link
# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time O(n) Space
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        def balanced(node):
            if not node : return 0
            left = balanced(node.left)
            right = balanced(node.right)
            if abs(left - right) > 1 : return float('inf')
            return 1+ max(left,right)
            
        return True if balanced(root) != float('inf') else False
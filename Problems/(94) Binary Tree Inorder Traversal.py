# Question Link
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Description
'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ---------------------------------- Recursive Soultion -------------------------------- #
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node , list):
            if node == None:
                return list

            inorder(node.left , list)
            list.append(node.val)
            return inorder(node.right , list)
        ans = []
        return inorder(root , [])



# ---------------------------------- Iterative Soultion -------------------------------- #
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        current = root
        while True:
            if current != None:
                stack.append(current)
                current = current.left
            
            elif stack:
                current = stack.pop()
                output.append(current.val)
                
                current = current.right
            
            else:
                return output
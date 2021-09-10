# Question Link
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Description
'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #-------------------------- Recursive Approach --------------------------------------#
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def pre(node, list):
            if node == None:
                return list
            list.append(node.val)
            pre(node.left, list)
            return pre(node.right, list)
            
        
        
        return pre(root, [])

    


    #-------------------------- iterative Approach --------------------------------------#
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        current = root
        while True:
            if current != None:
                output.append(current.val)
                stack.append(current)
                current = current.left
            elif stack :
                current = stack.pop()
                current = current.right
            else:
                return output
            
        
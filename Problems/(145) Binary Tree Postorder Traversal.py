# Question Link
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Description
'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ----------------------------- Recursive -------------------------------------------#
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node , list):
            if node == None:
                return list
            postorder(node.left , list)
            postorder(node.right , list)
            list.append(node.val)
            return list
        ans = []
        return postorder(root, ans)


    # --------------------------------- Iterative -----------------------------------------#
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s1 = []
        s2 = []
        output = []
        current = root
        s1.append(current)
        if current == None:
            return output
        while s1:
            current = s1.pop()
            s2.append(current)
            if current.left :
                s1.append(current.left)
            if current.right:
                s1.append(current.right)

            
        
        while s2:
            output.append(s2.pop().val)
        return output
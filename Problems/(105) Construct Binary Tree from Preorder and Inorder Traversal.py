# Question Link
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Description
'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dict = {v:i for i,v in enumerate(inorder)}
        q = deque(preorder)
      
        def construct(start, end ):
            if start > end:
                return
            else:
                element = q.popleft()

                root = TreeNode(element)
                mid = dict[element]
                root.left = construct(start,mid-1 )
                root.right = construct(mid+1, end )
                return root

        return construct(0,len(inorder)-1)
        
        
        
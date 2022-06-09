# Question Link
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time O(n) Space
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        
        root = TreeNode(preorder[0])

        node = root
        s = [root]
        for i in range(1,len(preorder)):
            node = TreeNode(preorder[i])
            if node.val < s[-1].val:
                s[-1].left = node
                s.append(node)
            else:
                while s and node.val > s[-1].val:
                    last_node = s.pop()
                last_node.right = node
                s.append(node)
        return root
                
                    
                
                
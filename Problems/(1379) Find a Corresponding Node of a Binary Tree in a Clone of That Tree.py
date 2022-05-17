# Question Link
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # O(n) Time O(n) Space
        def dfs(original,cloned):
            if not original :
                return None
            if original == target:
                return cloned
            right = dfs(original.right, cloned.right)
            left = dfs(original.left, cloned.left)
            return left if left else right
                

        return dfs(original,cloned)
# Question Link
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time O(d) Space
    def goodNodes(self, root: TreeNode) -> int:
        def dfs_with_max_value(node,max_val):
            if not node : return 0
            if node.val >= max_val :
                return 1 +  dfs_with_max_value(node.right,max(max_val,node.val)) +  dfs_with_max_value(node.left,max(max_val,node.val))
            return 0 +  dfs_with_max_value(node.right,max_val) + dfs_with_max_value(node.left,max_val)
        
        return dfs_with_max_value(root, float('-inf'))
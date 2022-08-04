# Question Link
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time O(1) Space
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,depth):
            if not node :
                return float("inf")
            if not node.right and not node.left :
                return depth
            return min(dfs(node.right,depth+1) , dfs(node.left,depth+1))

        return dfs(root,1) if  dfs(root,1) != float('inf') else 0
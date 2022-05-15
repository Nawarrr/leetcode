# Question Link
# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time 
    # O(d*2^d) Space While d is the depth of the tree a length d dict of O(2^d)
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        
        def dfs(node,level):
            if not node:
                return
            print(node.val)
            levels[level].append(node.val)
        
            dfs(node.right, level+1)
            dfs(node.left , level+1)

            return
        dfs(root,0)
        max_level = max(levels.keys())
        return sum(levels[max_level])
            
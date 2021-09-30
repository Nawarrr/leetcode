# Question Link
# https://leetcode.com/problems/binary-tree-right-side-view/

# Description
'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hash = defaultdict(list)
        def dfs(root,level, hash):
            if not root : return 
            hash[level].append(root.val)
            dfs(root.left,level+1,hash)
            dfs(root.right,level+1,hash)
            return 
        dfs(root,0,hash)
        output = []
        for i in hash.values():
            output.append(i[-1])
        return output
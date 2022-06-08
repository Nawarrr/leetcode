# Question Link
# https://leetcode.com/problems/cousins-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) Time O(1) Space
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node,val,depth,parent):
            if node == None:
                return None
            if node.val == val:
                return (depth,parent)
            
            return dfs(node.right, val,depth+1,node) or dfs(node.left, val,depth+1,node)
        
        xd,xp = dfs(root,x,0,None)
        yd,yp = dfs(root,y,0,None)
        return (xd == yd) and (xp != yp)
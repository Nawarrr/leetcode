# Question Link
# https://leetcode.com/problems/binary-tree-paths/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node,path,paths):
            if not node.right and not node.left :
                path += str(node.val)
                paths.append(path)


            if node.left :
                dfs(node.left,path + str(node.val) + '->',paths)
            if node.right :
                dfs(node.right,path + str(node.val) + '->',paths)

            return paths

        if not root : return []
        paths = []
        return dfs(root,"" , paths)
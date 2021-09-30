# Question Link
# https://leetcode.com/problems/path-sum-ii/

# Description
'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def sumToLeaf(root,sum,path, output):
            if not root: return 
            sum -= root.val
            path = path.copy()
            path.append(root.val)
            if sum ==0 and not root.left and not root.right :
                output.append(path)
                
            else:
                sumToLeaf(root.left,sum,path,output)

                sumToLeaf(root.right,sum,path,output)
                
            return output
        
        return sumToLeaf(root,targetSum,[],[])
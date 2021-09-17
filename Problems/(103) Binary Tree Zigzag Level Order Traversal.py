# Question Link 
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Description
'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return root
        queue = collections.deque()
        output = []
        queue.append(root)
        counter = 0
        while queue :
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    
            
            if level :
                if counter % 2 == 1:
                    level.reverse()
                output.append(level)
                
                    
            counter +=1
        return output
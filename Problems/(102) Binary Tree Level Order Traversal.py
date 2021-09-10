# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ------------------------------ Depth First Search ----------------------------- # 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We create a hash of lists , key ---> level , list for every level
        level_hash = defaultdict(list)
        
        def dfs(root , level):
            if root == None :
                return
            level_hash[level].append(root.val)
            dfs(root.left , level+1)
            dfs(root.right , level+1)
        
        dfs(root, 0)
        
        # We loop over the hash to extract every level 
        i = 0
        output = []
        while level_hash.get(i):
            output.append(level_hash.get(i))
            i += 1
        
        return output

    # ------------------------------ Breadth First Search ----------------------------- # 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        next_queue = []
        level = []
        output = []
        while queue:
            for node in queue:
                level.append(node.val)
                if node.left != None:
                    next_queue.append(node.left)
                if node.right != None:
                    next_queue.append(node.right)
            output.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return output
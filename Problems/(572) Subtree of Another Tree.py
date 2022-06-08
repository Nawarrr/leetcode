# Question Link
# https://leetcode.com/problems/subtree-of-another-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n*m) Time O(n) Space 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(p,q):
            if (not p and q)  or (not q and p):
                return False
            elif not p and not q : return True

            if p.val == q.val :
                return compare(p.right,q.right) and compare(p.left,q.left)
            else:
                return False
        q = deque()
        q.append(root)
        while q :
            node = q.popleft()
            if node:
                q.append(node.right)
                q.append(node.left)
                if node.val == subRoot.val:
                    if compare(node,subRoot): return True
        return False



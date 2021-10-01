# Question Link
# https://leetcode.com/problems/binary-search-tree-iterator/

# Description
'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root        
        self.stack =self.__partialInorder__(self.root,[])
        

    def __partialInorder__(self, root , stack):
        if not root:
            return
        stack.append(root)
        self.__partialInorder__(root.left , stack)
        return stack
    
    
    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return val
            

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
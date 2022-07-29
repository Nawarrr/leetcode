# Question Link
# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # O(n) Time and Space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = {}
        curr = head
        dummy_node = Node(0)
        new_curr = dummy_node
        while curr :
            if curr in lookup :
                new_curr.next = lookup[curr]
            else:
                new_head = Node(curr.val)
                lookup[curr] = new_head
                new_curr.next = new_head
            new_curr = new_curr.next
            if curr.random in lookup:
                new_curr.random = lookup[curr.random]
            else:
                
                new_random = Node(curr.random.val) if curr.random else None
                new_curr.random = new_random
                lookup[curr.random] = new_curr.random

            curr = curr.next
        
        return dummy_node.next
            
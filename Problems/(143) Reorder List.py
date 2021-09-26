# Question Link
# https://leetcode.com/problems/reorder-list/

# Description
'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        dummyNode = ListNode()
        dummyNode.next = head
        curr = head
        while curr:
            q.append(curr)
            curr = curr.next
        
        curr = q.popleft()
        curr.next = None
        dummyNode.next = curr
        state = False
        while q:
            if state:
                node = q.popleft()
                node.next = None
                curr.next = node
                curr = curr.next
                state = False
                
            if not state and q :
                node = q.pop()
                node.next = None
                curr.next = node
                curr = curr.next
                state = True
# Question Link
# https://leetcode.com/problems/middle-of-the-linked-list/

# Description
'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head.next
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
        return slow
        
# Question Link
# https://leetcode.com/problems/swap-nodes-in-pairs/


# Description
'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummyNode = ListNode()
        dummyNode.next = head
        prev , curr , next = dummyNode , head , head.next
        while prev and curr and next:
            curr.next = next.next
            prev.next = next
            next.next = curr
            
            prev = curr
            curr = curr.next
            if not curr:
                break
            next = curr.next
            
        return dummyNode.next
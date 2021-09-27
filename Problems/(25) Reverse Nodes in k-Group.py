# Question Link
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Description 
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head , k):
            prev , curr , next = None , head , None
            while curr and k > 0 :
                next = curr.next
                curr.next = prev
                
                prev = curr
                curr = next
                k-=1
            head = prev
            return head
        
        dummyNode = ListNode()
        dummyNode.next = head
        prev , curr = dummyNode , head
        while curr:
            tail = curr
            Index = 0
            while Index < k and curr :
                curr = curr.next
                Index+= 1
            if Index != k:
                prev.next = tail
            else:
                prev.next = reverse(tail , k)
                prev = tail
                
        return dummyNode.next
                
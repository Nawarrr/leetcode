# Question Link
# https://leetcode.com/problems/remove-linked-list-elements/

# Description
'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        curr , prev = head , dummy
        while curr:
            if curr.val == val :
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        return dummy.next
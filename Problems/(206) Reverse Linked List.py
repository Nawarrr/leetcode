# Question Link
# https://leetcode.com/problems/reverse-linked-list/

#Description
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next ==None:
            return head
        

        
        prev,curr, next = None , head , None

        while curr :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
                
    #--------------------------------- Recursive Approach ------------------------#
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(prev, head):
            if head == None:
                return prev
            next = head.next
            head.next = prev
            prev = head
            return reverse(head , next)
        
        return reverse(None , head)
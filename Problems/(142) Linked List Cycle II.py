# Question Link
# https://leetcode.com/problems/linked-list-cycle-ii/

# Description
'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



#  Solved using The Tortoise and the Hare Algorithm (Floyd's) , Check it
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head : return
        slow = head
        fast = head
        condition = False
        while fast.next and fast.next.next :
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                condition = True
                
                break

        
        if not condition : return
        
        while True :
            if fast == slow :
                return fast
            fast = fast.next
            slow = slow.next
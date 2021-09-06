# Question Link
# https://leetcode.com/problems/linked-list-cycle/submissions/

# Description
'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# ------------------ O(n) Time O(n) Space--------------------#
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        list_hash = {}

        while  head != None :
            if list_hash.get(head):
                return True 
            else:
                list_hash[head] = True
                head = head.next
        return False

# ------------------ O(n) Time O(1) Space--------------------#
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head 
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        return False
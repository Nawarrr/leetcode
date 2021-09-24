# Question Link
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Description
'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummyNode = ListNode(101)
        dummyNode.next = head
        prev = dummyNode
        curr = head
        value = 102
        while curr and curr.next :
            if  curr.val == value or curr.val == curr.next.val:
                value = curr.val
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        if curr.val == value:
            prev.next = None
        return dummyNode.next
# Question Link
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Description
'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #if head.next == None:
            #return head.next
            
        dummy = slow = fast = ListNode(0,next=head) 
         
        
        for i in range(n):
            fast = fast.next
        
        while slow:
            if fast.next == None:
                slow.next = slow.next.next
                break
            else:
                slow = slow.next
                fast = fast.next
        return dummy.next
        
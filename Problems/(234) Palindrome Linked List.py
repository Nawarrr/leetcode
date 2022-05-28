# Question Link
# https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) Time O(1) Space
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # get the len of the list in O(n)
        curr = head
        length = 0
        while curr :
            length+=1
            curr = curr.next
        
        
        
        midpoint = (length//2)  if length % 2 == 0 else (length//2)+1
        
        # Reverse the second half O(n)
        curr = head
        for i in range(midpoint):
            curr = curr.next
        
        
        newhead = curr
        prev = None
        while newhead :
            next = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = next
        
        # Compare the 2 halfs
        curr1 =head
        curr2 =prev
        half = length//2
        while curr1 and curr2 and half :
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
            half-=1
        return True
        
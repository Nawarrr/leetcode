# Question link
#https://leetcode.com/problems/add-two-numbers/

#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order, and each of their nodes
# contains a single digit.
#Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.


#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
        self.next = next
class Solution:
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = output = ListNode()
        carry = 0
        while l1 and l2 :
            output.next = ListNode()
            output = output.next
            n1 = l1.val
            n2 = l2.val
            if (n1 +n2 + carry) >9:
                
                output.val = (n1 +n2 + carry) % 10
                carry = 1
            else:
                output.val = (n1 +n2 + carry)
                carry = 0
            l1 = l1.next
            l2 = l2.next
    
                
                
                
        while l1 :
            output.next = ListNode()
            output = output.next
            if l1.val + carry >9:
                output.val = 0
                carry = 1
            else:
                output.val = l1.val + carry
                carry = 0
            l1 = l1.next
        while l2 :
            output.next = ListNode()
            output = output.next
            if l2.val + carry >9:
                output.val = 0
                carry = 1
            else:
                output.val = l2.val + carry
                carry = 0
            l2 = l2.next
        if carry:
            output.next = ListNode(1)
            
        return dummy.next

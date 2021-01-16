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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        curr = l3
        carry = 0
        while l2 != None or l1 != None :
            if l1 == None:
                curr.next = ListNode( (l2.val + carry) % 10 )
                curr = curr.next
                if l2.val + carry == 10:
                    carry = 1
                else:

                    carry = 0
                l2 = l2.next
            elif l2 == None:
                curr.next = ListNode( (l1.val+ carry) %10)
                curr = curr.next
                if l1.val + carry == 10:
                    carry = 1
                else:
                    carry = 0

                l1 = l1.next
            else:
                if l2.val + l1.val + carry > 9:
                    curr.next = ListNode((l2.val + l1.val + carry) % 10  )
                    carry = 0
                    curr = curr.next
                    carry += 1
                    l1 = l1.next
                    l2 = l2.next
                else:
                    curr.next = ListNode(l2.val + l1.val + carry)
                    carry = 0
                    curr = curr.next
                    l1 = l1.next
                    l2 = l2.next

            if carry != 0 :
                curr.next = ListNode(carry)
        return l3.next

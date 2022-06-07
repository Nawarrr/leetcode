# Question Link
# https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) Time O(1) Space
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head  or not head.next: return head
        # Tail pointer and length of the list
        curr = head
        length = 0
        while curr.next:
            length+=1
            curr = curr.next
        tail = curr
        
        
        # Moving Even
        prev = head
        curr = head.next
        
        while curr.next and length > 0 :
            
            # Removing node
            node = curr
            next = curr.next
            prev.next = next
                
            # Adding node at the end
            tail.next = node
            node.next = None
                
                
            # next iteration
            tail = tail.next
            curr = next.next
            prev = next
            
            length-=2
            
            
        return head
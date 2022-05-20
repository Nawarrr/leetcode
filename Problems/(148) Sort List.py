# Question Link
# https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # O(nLogn) Time O(n) Space
    # I'm not sure wither Timsort uses O(n) or O(nLogn) Space
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        temp = []
        while curr :
            temp.append((curr.val,curr))
            curr = curr.next
        
        temp.sort(key=itemgetter(0))
        dummyNode = ListNode()
        curr = temp[0][1]
        dummyNode.next = curr
        for i in range(1,len(temp)):
            curr.next = temp[i][1]
            curr = curr.next
        curr.next = None
        return dummyNode.next
        
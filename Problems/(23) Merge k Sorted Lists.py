# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(nK) time O(1) Space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists : return None
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            if not l1 and not l2 : return None
            if l1 and not l2 : return l1
            if l2 and not l1 : return l2 
            dummyNode = ListNode()
            curr1,curr2 = l1,l2
            curr3 = dummyNode
            while curr1 and curr2 :
                if curr1.val > curr2.val :
                    curr3.next = curr2
                    curr2 = curr2.next
                else:
                    curr3.next = curr1
                    curr1 = curr1.next
                curr3 = curr3.next
            if curr1 : curr3.next = curr1 
            if curr2 : curr3.next = curr2
            return dummyNode.next
        
        for i in range(1,len(lists)):
            lists[i] = mergeTwoLists(lists[i-1] , lists[i])
        
        return lists[-1]
    
    # There is a better approach, O(nLogk) as a Divide and Conquer approach
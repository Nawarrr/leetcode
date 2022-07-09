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
        

# -------------------------------- O(Logn) Time O(1) Space -------------- Most Optimal Using  Merge Sort ------------------------------------# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.

        def mergeSort(lst):
            if not lst or not lst.next : return lst
            l1,l2 = list_split(lst)
            left = mergeSort(l1)
            right = mergeSort(l2)
            return merge(left,right)

        def list_split(lst):
            
            slow  = lst 
            fast = lst.next
            while fast and fast.next :

                slow = slow.next
                fast = fast.next.next
           
            l2 = slow.next
            slow.next = None
            l1 = lst
            return l1,l2





        def merge(l1,l2):
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

        curr = head
        return mergeSort(curr)
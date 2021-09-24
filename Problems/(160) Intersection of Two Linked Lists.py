    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        #--------------------------------------- O(N) time , O(n) space -----------------------------------# 
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            hash = {}
            while headA:
                hash[headA] = True
                headA = headA.next
            while headB :
                if hash.get(headB):
                    return headB
                headB = headB.next
        #--------------------------------------- O(N) time , O(1) space -----------------------------------# 
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            currA,currB = headA,headB
            countA,countB = 0,0
            # Counting Both of them
            while currA:
                countA += 1
                currA = currA.next
            
            while currB:
                countB += 1
                currB = currB.next
                
            diff = countA-countB
            # Moving the Diffrence (Unclean AF way to do it, I can do better but fuck it who cares)
            if countA > countB :
                diff = countA-countB
                currA = headA
                for i in range(diff):

                    currA = currA.next
                currB = headB
                
            else:
                diff = countB-countA
                currB =headB
                for i in range(diff):

                    currB = currB.next
                currA = headA
            # Moving them together 
            while currA and currB:
                if currA == currB:
                    return currA
                currA = currA.next
                currB = currB.next
            


            #--------------------------------------- O(N) time , O(1) space -----------------------------------# I'm in Fucking Love with this solution
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            currA = headA
            currB = headB

            while currA or currB:
                
                if currA == None:
                    currA = headB
                    
                if currB == None:
                    currB = headA
                    
                if currA == currB :
                    return currA

                currA = currA.next
                currB=currB.next
                


            
            return None
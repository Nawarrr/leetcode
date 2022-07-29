# Question Link
# https://leetcode.com/problems/koko-eating-bananas/


class Solution:
    # O(nLogn) Time O(1) Space
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k,h):
            i = 0
            while h>=0 :
                if i == len(piles):
                    return True
                h-= ceil(piles[i] / k)
                i+=1
            return False
        
        l = 1
        r = max(piles)
        while l < r:
            mid = (l+r)//2
            if not eat(mid,h) :
                l = mid+1
            else :
                r = mid
        return l
        
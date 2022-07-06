# Question Link
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        shorizontalCuts = sorted(horizontalCuts)
        sverticalCuts = sorted(verticalCuts)

        max_h = 0
        max_v = 0     
        
        for i in range(1 , len(shorizontalCuts)):
            max_h = max(max_h,shorizontalCuts[i] - shorizontalCuts[i-1])
        
        for i in range(1 , len(sverticalCuts)):
            max_v = max(max_v,sverticalCuts[i] - sverticalCuts[i-1])
        
        return (max_v*max_h)  % (10**9+7)
            
            
# Question Link
# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1 : return x 
        low = 0
        high = x 
        
        while True :
            mid = (high + low) //2

            if x == mid**2 or (x > mid**2) and (x < (mid+1)**2):
                return mid
            elif x < mid**2:
                high = mid+1
            else:
                low = mid
        return mid
                
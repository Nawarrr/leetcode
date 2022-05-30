# Question Link
# https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        di = abs(divisor)
        ans = 0
        while d >= di:
            temp = di
            mul = 1
            while d >= temp:
                d -= temp
                ans += mul
                mul <<=  1
                temp <<=  1
                
        if(dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            ans = - ans
                
        return min(2147483647,max(-2147483648,ans))
            
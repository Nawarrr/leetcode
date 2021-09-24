# Question Link
# https://leetcode.com/problems/climbing-stairs/


# Description
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]

        for i in range(2,n):
            dp.append(dp[i-1] + dp[i-2])
        print(dp)
        return dp[n-1]
            
        

        
        
        
        

            
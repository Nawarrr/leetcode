# Question Link
#https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        
        
        for i in range(amount+1):
            for coin in coins:
                if i-coin >=0 :
                    dp[i] = min(dp[i] , dp[i-coin]+1)
        
        return -1 if dp[-1] == float('inf') else dp[-1]
            
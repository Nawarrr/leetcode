class Solution:
    #---------------------------------------- O(n Log n) ----------------------------------------# 
    def count(self, n: int) -> List[int]:
        nums = []
        for i in range(n+1):
            counter = 0
            while i != 0:
                one = i % 2
                if one : counter +=1
                i = i //2
            nums.append(counter)
        return nums
    #----------------------------------------     O(n)     ----------------------------------------# Using  DP 
    def count(self, n: int) -> List[int]:
        import math
        dp = [0]
        power = 0
        for i in range(1,n+1):
            if math.log(i,2).is_integer()  :
                power = i

            dp.append(1 + dp[i-power]) 
        return dp

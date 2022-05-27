# Question Link
# https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    # O(nLogn) Time O(n) Space 
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        s_env = sorted(envelopes , key=lambda x:(x[0],-x[1]))
        
        
        dp = []
        
        for w,h in s_env:
            i = bisect_left(dp,h)
            
            if i == len(dp):
                dp.append(h)
            else:
                dp[i]=h
        

        return len(dp)

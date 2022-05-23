# Question Link
# https://leetcode.com/problems/ones-and-zeroes/



class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        N = len(strs)
        
        
        zeros = [0 for _ in range(N+1)] 
        ones = [0 for _ in range(N+1)] 
        
        for i in range(N):
            zeros[i] = strs[i].count("0")
            ones[i] = strs[i].count("1")
        
        memo = {}
        def count(index , zeros_left,ones_left):
            if index == N :
                return 0
            
            if (index,zeros_left,ones_left) in memo :
                return memo[index,zeros_left,ones_left]
            
            best = 0
            if zeros_left >= zeros[index] and ones_left >= ones[index]:
                best = max(best , count(index+1 , zeros_left- zeros[index] , ones_left - ones[index]) +1)
            
            best = max(best , count(index+1 , zeros_left , ones_left))
            
            memo[index,zeros_left,ones_left] = best
            return best
        
        return count(0,m,n)
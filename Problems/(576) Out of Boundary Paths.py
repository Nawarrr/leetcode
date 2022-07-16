# Question Link
# https://leetcode.com/problems/out-of-boundary-paths/


class Solution:
    # O(n*m*moves) space and time
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        lookup = {}
        def dfs(i,j,moves_left):
            if (i,j,moves_left) in lookup : return lookup[(i,j,moves_left)]
            if moves_left < 0 :
                return 0
            if i < 0 or j < 0 or i >= m or j >= n :
                return 1
            
            lookup[(i,j,moves_left)] = dfs(i+1,j,moves_left-1)+dfs(i,j+1,moves_left-1)+dfs(i-1,j,moves_left-1)+dfs(i,j-1,moves_left-1)
            
            return lookup[(i,j,moves_left)]
        
        return dfs(startRow,startColumn,maxMove) % (10**9 + 7)
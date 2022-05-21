# Question Link
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    # O(n*m) Time O(n*m) Space
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        steps = [(-1,0) , (0,-1) , (1,0) , (0,1)]
        @lru_cache
        def dfs(i,j):
            longest = 1 
            for x,y in steps:
                if  0 <= i+x < m and 0<= j+y < n and  matrix[i][j] < matrix[i+x][j+y]:
                    longest = max(longest , 1+dfs(i+x,j+y))
            return longest
            
                    
        output = 1
        for i in range(m):
            for j in range(n):
                output = max(output , dfs(i,j))
        return output
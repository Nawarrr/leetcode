# Question Link
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    # O(m*n) time  O(m*n) Space 
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        @lru_cache
        def dfs(i,j):
            if i>= m or j>=n or obstacleGrid[i][j] == 1 :
                return 0
            if i == m-1 and j ==n-1:
                return 1
            return dfs(i+1,j) + dfs(i,j+1)
        
        
        return dfs(0,0)
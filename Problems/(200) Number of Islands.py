# Question Link
# https://leetcode.com/problems/number-of-islands/

# Description
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)]for _ in range(m)]
        
        def visit(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0" or visited[i][j]  :
                return
            
            else:
                visited[i][j] = True
                visit(i+1,j)
                visit(i-1,j)
                visit(i,j+1)
                visit(i,j-1)
        count = 0
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    visit(i,j)
                    count += 1
                    
                    
        return count
                
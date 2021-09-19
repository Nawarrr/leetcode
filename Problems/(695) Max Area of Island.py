# Question Link
# https://leetcode.com/problems/max-area-of-island/

# Description
'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        count = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited.get((i,j)) or grid[i][j]==0:
                return 0
            
            visited[(i,j)] = True
            return 1 + dfs(i+1 ,j)+ dfs(i-1 ,j) + dfs(i ,j+1) + dfs(i ,j-1)
            
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not visited.get((i,j)):
                    
                    count = max(count ,dfs(i,j) )
        return count
# Question Link
# https://leetcode.com/problems/island-perimeter/

# Description

'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    startr , startc = i,j
                    break
            
            if grid[i][j] == 1:
                break
        
        visited = [[False for _ in range(col)] for _ in range(row)]
        self.per = 0
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= row or j >= col:
                self.per+=1
                return
            if visited[i][j]:
                return
            
            
            if grid[i][j] == 0:
                self.per+=1
                return
            visited[i][j] = True
            dfs(i+1,j)
            dfs(i , j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            return
        dfs(startr,startc)
        
        return self.per
                
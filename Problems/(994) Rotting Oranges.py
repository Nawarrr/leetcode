# Question Link
# https://leetcode.com/problems/rotting-oranges/

# Description
'''
You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
        minute = 0
        prev = fresh
        while True:
            grid_copy = copy.deepcopy(grid)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] ==2 :
                        for r,c in [(i-1 , j) , (i+1,j), (i,j-1) , (i , j+1)]:
                            if  0<=r<m and 0<=c<n and grid_copy[r][c]==1:
                                grid_copy[r][c]=2
                                fresh -=1
            if prev == fresh:
                break
            minute += 1
            grid = grid_copy
            prev = fresh
        if fresh > 0:
            return -1
        else:
            return minute
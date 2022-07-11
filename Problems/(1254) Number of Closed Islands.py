# Question Link
# https://leetcode.com/problems/number-of-closed-islands/


class Solution:
    # O(n*m) Time and Space
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        v = len(grid)
        h = len(grid[0])
        count = 0

        
        def dfs(i,j):
            if i >= v or j >= h or i < 0 or j < 0 :
                return False
            if grid[i][j] == 1 or (i,j) in visited :
                return True
            visited[(i,j)] = True
            right = dfs(i+1,j) 
            down = dfs(i,j+1)
            left = dfs(i-1,j)
            up = dfs(i,j-1)
            
            return right and down and left and up
        
        for i in range(v):
            for j in range(h):
                if (i,j) not in visited :
                    island = dfs(i,j)
                    if grid[i][j] == 0  and island:
                        count+=1
                    
        return count
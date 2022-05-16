# Question Link
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        q = deque()
        
        directions = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1)]
        
        if grid[0][0] == 0:
            visited.add((0,0))
            q.append((1 ,(0,0)))
        while q :
            cost,index = q.popleft()
            i,j = index
            if (i,j) == (n-1,n-1):
                return cost
            for x,y in directions:
                new_i , new_j = i+x , j+y 
                if new_i>=0 and new_j>=0 and new_i<n and new_j <n and (new_i,new_j) not in visited and grid[new_i][new_j] == 0 :
                    q.append((cost+1,(new_i,new_j)))
                    visited.add((new_i,new_j))
                
        return -1
            

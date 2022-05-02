# Question Link
# https://leetcode.com/problems/number-of-provinces/

# Description
'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        visited = [False for i in range(n)]
        count = 0
        def visit(i):
            if visited[i] == True :
                return
            visited[i] = True
            for ind,v in enumerate(isConnected[i]):
                if ind != i and v ==  1:
                    visit(ind)
        
        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1 and visited[i] == False :
                    visit(i)
                    count +=1
        return count 
                
            
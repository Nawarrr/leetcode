# Question Link
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1 : return -1
        
        graph = defaultdict(list)
        
        for connection in connections :
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
            
        visited = [False for _ in range(n)]
        
        count = 0
        
        
        def dfs(i):
            if visited[i] : return 
            visited[i] = True
            for j in graph[i]:
                dfs(j)
            return
        
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)
        
        return count-1
            

            
        
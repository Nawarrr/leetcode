# Question Link
# https://leetcode.com/problems/critical-connections-in-a-network/

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        for u,v in connections:
            g[u].append(v)
            g[v].append(u)
            
        
        time = [0 for _ in range(n)]
        low = [0 for _ in range(n)]
        ans=[]
        def dfs(g, curr, parent,count):
            count+=1
            time[curr]=count
            low[curr]=count
            for next in g[curr]:
                if next == parent: continue
                if time[next]==0:
                    dfs(g,next,curr,count)
                    low[curr] = min(low[curr] , low[next])
                else:
                    low[curr] = min(low[curr] , low[next])
                if low[next] > time[curr]:
                    ans.append((curr,next))
        dfs(g,0,-1,0)            
        return ans
                
            
                
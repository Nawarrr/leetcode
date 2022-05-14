# Question Link
# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        
        for u,v,w in times :
            edges[u].append((v,w))
        
        heap = [(0,k)]
        visited = set()
        cost = 0
        
        while heap :
            w,u = heapq.heappop(heap)
            if u in visited : continue
            visited.add(u)
            cost = max(cost,w)
            for node,EdgeCost in edges[u]:
                if node not in visited:
                    heapq.heappush(heap,(w+EdgeCost,node))
        
        if len(visited) != n: return -1
        else: return cost
                        
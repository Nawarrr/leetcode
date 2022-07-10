# Question Link
# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            if color[i] != -1 : continue
            q = deque()
            q.append((i,0))

            while q:
                node= q.popleft()
                if color[node[0]] == -1:
                    color[node[0]] = node[1]
                    for n in graph[node[0]]:
                        ncol = 0 if node[1] else 1
                        q.append((n,ncol))
                else:
                    if node[1] != color[node[0]]:
                        return False
        return True
        
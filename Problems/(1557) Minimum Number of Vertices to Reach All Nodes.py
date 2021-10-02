# Question Link
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# Description
'''
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
'''
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [False] * n
        for a,b in edges :
            count[b] +=1
        output = []
        for i in range(n):
            if not count[i]:
                output.append(i)
        return output
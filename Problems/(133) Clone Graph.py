# Question Link
# https://leetcode.com/problems/clone-graph/


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # O(E+V) time O(V) Space
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node : return None
        visited = {}
        def dfs(node):
            new_node = Node(node.val)
            visited[node.val] = new_node 
            nghbr = []
            
            for n in node.neighbors:
                if n.val in visited :
                    nghbr.append(visited[n.val])
                else:
                    nghbr.append(dfs(n))
                    
            new_node.neighbors = nghbr
            return new_node
        return dfs(node)
            
                    
            
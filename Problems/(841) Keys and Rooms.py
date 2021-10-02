# Question Link
# https://leetcode.com/problems/keys-and-rooms/

# Description
'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
'''
# Breadth First Search
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        visited = {}
        q.append(0)
        while q:
            room = q.pop()
            if not visited.get(room):
                visited[room] = True
                for key in rooms[room]:
                    q.append(key)
        if len(visited) == len(rooms):
            return True
        else:
            return False
# Depth First Search
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = {}
        def dfs(room):
            if visited.get(room):
                return
            visited[room] = True
            for key in rooms[room]:
                dfs(key)
            
        dfs(0)
        return len(visited) == len(rooms)
            
            
            
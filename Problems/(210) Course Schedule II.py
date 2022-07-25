# Question Link
# https://leetcode.com/problems/course-schedule-ii/


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        # Construct Graph
        for preq in prerequisites:
            graph[preq[1]].append(preq[0])
        
        
       # visited = [False for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            for c in graph[i]:
                indegree[c]+=1
        top = []
        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q :
            c = q.popleft()
            top.append(c)
            for course in graph[c]:
                indegree[course]-=1
                if indegree[course] == 0:
                    q.append(course)
        
        return top if len(top) == numCourses else []
            
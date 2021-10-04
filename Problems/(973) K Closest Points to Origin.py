# Question Link
# https://leetcode.com/problems/k-closest-points-to-origin/

# Description

'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_distance = []
        for point in points :
            point_distance.append((sqrt(point[0]**2 +point[1]**2 ) , point))
        heapq.heapify(point_distance)
        output = []
        for i in range(k):
            output.append(heapq.heappop(point_distance)[1])
        return output
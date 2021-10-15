#Question link
#https://leetcode.com/problems/container-with-most-water/

# Description
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''


# Greedy Soultion


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1
        maxArea = 0
        while i < j :
            area = min(height[i] , height[j])* (j-i)
            maxArea = max(maxArea,area)
            if height[i] > height[j]:
                j -=1
            else:
                i+=1
        return maxArea
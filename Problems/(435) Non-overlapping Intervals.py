# Question Link
# https://leetcode.com/problems/non-overlapping-intervals/

# Description
'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        intervals.sort(key=lambda x: x[1])
        max_end = float('-inf')
        for i in intervals:
            if i[0] >= max_end:
                max_end = i[1]
            else:    
                counter +=1
        print(intervals)
        return counter

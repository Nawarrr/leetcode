# Question Link
# https://leetcode.com/problems/merge-intervals/

# Description
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort()
        
        output = [intervals[0]]
        for s,e in intervals[1:]:
            if s > output[-1][1]:
                output.append([s , e])
            elif e > output[-1][1]:
                output[-1][1] = e
                                      
        return output
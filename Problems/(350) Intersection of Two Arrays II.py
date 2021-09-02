# Question Link
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Description 
"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        intersection = []
        for i in nums1:
            if hash.get(str(i)):
                hash[str(i)] +=1
            else:
                hash[str(i)] = 1
        
        for i in nums2:
            if hash.get(str(i)):
                intersection.append(i)
                hash[str(i)] -=1
        
        return intersection                
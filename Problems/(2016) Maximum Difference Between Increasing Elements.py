# Question Link
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/


# Description
'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
'''
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxSoFar = -1
        smallestElement = nums[0]
        for i in range(len(nums)):
            if nums[i] > smallestElement:
                
                maxSoFar = max(maxSoFar ,nums[i] - smallestElement )
                
            if nums[i] < smallestElement :
                smallestElement = nums[i]
        return maxSoFar
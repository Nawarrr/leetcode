# Question Link
# https://leetcode.com/problems/increasing-triplet-subsequence/

# Description
'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        small = nums[0]
        med = float('inf')
        for i in range(len(nums)):
            if nums[i] > med:
                return True
            elif nums[i] > small:
                med = nums[i] 
            else:
                small = nums[i]
        return False
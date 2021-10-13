# Question Link
# https://leetcode.com/problems/find-peak-element/

# Description
'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l < r :
            mid = (l+r) //2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return l
            
        
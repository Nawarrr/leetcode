# Question Link
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Description
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        if n ==0 : return [-1,-1]
        l,r = 0 , n
        st,end = -1,-1
        
        # Left Binary Search
        while l <r :
            mid = (l+r) //2
            if nums[mid]>= target:
                r = mid
            else:
                l = mid+1
        if l < n and nums[l] == target: st = l
            
            
        l,r = 0 , n
        while l <r :
            mid = (l+r) //2
            if nums[mid]<= target:
                l = mid+1
            else:
                r = mid
        if nums[r-1] == target: end = r-1
        
        return [st,end]
        
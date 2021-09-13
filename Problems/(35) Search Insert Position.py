# Question Link
# https://leetcode.com/problems/search-insert-position/

# Description
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while high >= low:
            mid = (low+high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid +1
            elif target < nums[mid]:
                high = mid -1
        if target >nums[mid]:
            return mid +1
        else:
            return mid  
# Question Link
# https://leetcode.com/problems/search-in-rotated-sorted-array/




# Description
'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search for mid element
        n = len(nums)
        l,r= 0,n-1
        start = -1
        while l <r:
            mid = (l+r) //2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        start = l
        
        l,r= 0,n-1


        while l <= r:
            mid = (l+r) //2
            realMid = (mid+start) % n

            if nums[realMid] == target:
                return realMid
            elif nums[realMid] > target:
                r = mid -1
                
            else:
                
                l = mid +1 
            
            
                
        return -1
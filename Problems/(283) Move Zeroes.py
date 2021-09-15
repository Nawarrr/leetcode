# Question Link
# https://leetcode.com/problems/move-zeroes/

# Description 
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        x = len(nums)
        while i < x:
            if nums[i] == 0:
                del nums [i]
                nums.append(0)
                x -= 1
            else:
                i +=1
    

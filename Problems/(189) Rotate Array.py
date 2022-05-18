# Question Link
# https://leetcode.com/problems/rotate-array/

# Description
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = k% len(nums)
        
        def rev(s,e):
            while s<e:
                nums[s],nums[e]= nums[e],nums[s]
                s += 1
                e -=1
        nums.reverse()
 
        rev(0 , x-1)
     
        rev(x , len(nums)-1)

# Alternate Solution 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(1) Space Solution O(n) Soltion
        x = len(nums) - k if k < len(nums) else len(nums) - (k % len(nums))
        for i in range(x):
            num = nums[0]
            del nums[0]
            nums.append(num)
        return nums
            
            
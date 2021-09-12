# Question Link
# https://leetcode.com/problems/majority-element/


# Description
'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ----------------------------------------- O(n) Time O(n) Space --------------------------------------#
       hash = collections.Counter(nums)
       for i in hash.keys():
            if hash[i] > (len(nums) /2):
                return i
        # ----------------------------------------- O(n) Time O(1) Space --------------------------------------#
    
        majority = nums[0]
        count = 0
        for i in nums:
            if majority == i:
                count +=1
            elif count == 0:
                majority = i
            else:
                count -= 1
        return majority
            
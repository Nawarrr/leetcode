# Question Link
# https://leetcode.com/problems/single-number/


# Description
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result ^= i
            
        return result
        


# BITWISE MANIPULATION 
# Example
# [1 , 2 , 4 , 2 , 4]
# 0 ^ 1 = 1
# 01 ^ 10 = 11
# 011 ^ 110 = 101
# 101 ^ 010 = 111
# 111 ^ 110 = 001 = 1 
# Question Link
# https://leetcode.com/problems/squares-of-a-sorted-array/

# Description
'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order
'''
# Disclaimer : This is an  Ugly AF soultion but it's Optimal so who cares

# ------------------------------------------------------------------------- O(n)-------------------------------------------------------#
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(n) to get the zero place
        for i in range(len(nums)):
            if nums[i] >= 0:
                index_non_neg = i
                break
            if i == len(nums)-1:
                squared = [num ** 2 for num in nums]
                return reversed(squared)
        
        output = []
        i = index_non_neg -1
        j = index_non_neg 
        # O(n)
        while i >= 0 and j <= len(nums)-1 :
            if nums[i]**2 <= nums[j]**2:
                output.append(nums[i]**2)
                i -=1
            else:
                output.append(nums[j]**2)
                j +=1
        # O(n)
        while i >= 0 :
            output.append(nums[i]**2)
            i -=1
        # O(n)
        while j <= len(nums)-1:
            output.append(nums[j]**2)
            j +=1
        return output
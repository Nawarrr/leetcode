#Question link
#https://leetcode.com/problems/two-sum/

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        output = []
        for i,num in enumerate(nums):
            if target - num in nums and len(output) < 2 :

                if target- num != num:

                    output.append(i)
                elif nums.count(num) > 1:
                     output.append(i)
        return output        

# Question Link
# https://leetcode.com/problems/running-sum-of-1d-array/

# Descryption
#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        for i in range(0, len(nums)) :
            sum = nums[i] + sum
            nums[i] = sum
        return nums
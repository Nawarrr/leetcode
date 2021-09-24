# Question Link
# https://leetcode.com/problems/house-robber/


# Description
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [nums[0] , max(nums[1] ,nums[0]) ]
        for i in range(2 , len(nums)):
            dp.append(max(nums[i]+ dp[i-2] , dp[i-1]))
        return dp[-1]
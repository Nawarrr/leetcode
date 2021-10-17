# Question Link
# https://leetcode.com/problems/minimum-size-subarray-sum/

# Description
'''
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right = 0,0
        n = len(nums)
        curSum = 0
        ans = float('inf')
        while right < n :
            curSum += nums[right]
            
            while curSum >= target :
                ans = min(ans , right - left +1)

                curSum -= nums[left]
                left+=1
            right+=1
            
        ans = ans if ans != float('inf') else 0
        return ans
# Question Link
# https://leetcode.com/problems/subarray-sum-equals-k/

# Description
'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {}
        sum = 0
        hash[0] = 1
        count = 0
        for i in nums:
            sum += i
            if hash.get(sum-k):
                count += hash[sum- k ]
            hash[sum] = hash.get(sum , 0) +1
        return count 
                
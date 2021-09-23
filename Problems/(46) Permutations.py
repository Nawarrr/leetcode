# Question Link
# https://leetcode.com/problems/permutations/

# Decsription
'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(perm , array):
            if len(perm) == len(nums):
                output.append(perm.copy())
                return
            for i in range(len(array)):
                perm.append(array[i])
                backtrack(perm , array[0:i] + array[i+1:len(array)])
                perm.pop()
        backtrack([] , nums)
        return output
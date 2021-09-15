# Question Link
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Description
'''
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers)-1
        while s < e:
            if numbers[s] + numbers[e] == target:
                return [s+1 ,e+1]
            elif numbers[s] + numbers[e] > target:
                e -=1
            else:
                s +=1
        
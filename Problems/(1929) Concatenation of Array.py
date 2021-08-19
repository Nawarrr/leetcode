# Question Link
# https://leetcode.com/problems/concatenation-of-array/

# Descryption
#Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#Specifically, ans is the concatenation of two nums arrays.
#Return the array ans.

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #ans = []
        #for j in range(0,2):
        #    for i in nums :
        #        ans.append(i)
        #return ans
        return nums*2
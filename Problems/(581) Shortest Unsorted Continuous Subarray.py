# Question Link
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution(object):
    # O(N) Time , O(1) Space
    def findUnsortedSubarray(self, nums):
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        endIndex = 0
        # End Index
        for i in range(len(nums)):
            if nums[i] < prev:
                endIndex = i
            else:
                prev = nums[i]
        
        
        if endIndex == 0:
            return 0
        
        # Start Index
        prev = nums[-1]
        startIndex = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > prev:
                startIndex = i
            else:
                prev = nums[i]
        return endIndex-startIndex+1
    


    # O(nlogn) Time , O(n) Space
    def findUnsortedSubarray(self, nums):

        sortednums = sorted(nums)
        startIndex = endIndex = 0
        for i in range(0,len(nums)):
            if nums[i] != sortednums[i]:
                startIndex = i
                break
        for i in range(len(nums)-1, -1,-1):
            if nums[i] != sortednums[i]:
                endIndex = i
                break
        if endIndex == 0 :
            return 0
        else:
            return endIndex-startIndex+1
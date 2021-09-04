# Question Link
# https://leetcode.com/problems/maximum-subarray/
# Description
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.







# ------------------ DIVIDE AND CONQUER SOULTION FOR PRACTIVE ------------------------#
class Solution:
    
    def evaluateCrossingSum(self,array,left, mid,right):

        sum = 0
        # Left
        sumL = -1000000000000
        for i in range(mid, left-1 , -1):
            sum = sum + array[i]
            sumL = max(sum , sumL)
    
        # Right
        sumR = -100000000000000000
        sum = 0
        for i in range(mid+1 ,right + 1):
            sum = sum + array[i]
            sumR = max(sum , sumR)
            
        return max(sumL,sumR , sumL+sumR)
    def evaluateSumRL(self,array,left,right):
        if left == right :
            return array[0]
        mid = (right+left) //2
        
        
        return max(self.evaluateSumRL(array , left , mid) , 
                   self.evaluateSumRL(array,mid+1 , right) ,
                   self.evaluateCrossingSum(array, left, mid, right))
    def maxSubArray(self, nums: List[int]):
                   
        return self.evaluateSumRL(nums , 0 , len(nums)-1)
    
    
# ---------------- O(n) Kadane's Algorithm -------------#
    def maxSubArray(self, nums: List[int]):
        maxSoFar = -1000000000000
        maxHere = 0
        for i in nums:
            maxHere += i
            maxSoFar = max(maxHere,maxSoFar)
            if maxHere < 0 :
                maxHere = 0

        return maxSoFar
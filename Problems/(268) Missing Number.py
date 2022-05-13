# Question Link
# https://leetcode.com/problems/missing-number/

class Solution:
    # Approach 1 : Normal Loops,  O(n) Time O(1) Space
    def missingNumber(self, nums: List[int]) -> int:
        summ = sum(nums) # O(n) Time
        real_sum = 0
        for i in range(1,len(nums)+1):  # O(n) Time
            real_sum+=i
            
        return real_sum-summ


    # Approach 2 XOR : O(n) Time , O(1) Space
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(1,len(nums)+1):
            x^=i
        for i in nums:
            x^=i
        return x
        
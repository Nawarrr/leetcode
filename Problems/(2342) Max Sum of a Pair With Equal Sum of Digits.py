# Question Link 
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        #nums.sort(reverse=True)
        def sum_of_digits(num):
            sd = 0
            while num > 0 :
                sd += num % 10
                num = num // 10
            return sd
        
        sum_of_digts = [sum_of_digits(num) for num in nums]
        hsh = {}
        mx = -1
        for i,s in enumerate(sum_of_digts):
            if s in hsh :
                mx = max(mx,nums[i]+hsh[s])
                hsh[s] = max(nums[i],hsh[s])
            else:
                hsh[s] = nums[i]
        return mx
               
        
# Question Link
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/



class Solution:
    # O(n) Time O(1) Space
    def minOperations(self, nums: List[int], x: int) -> int:

    
        goal = sum(nums) - x
        max_len = -1
        curr_sum = 0
        j = 0
        
        for i,num in enumerate(nums):
            curr_sum+= num 
            
            while curr_sum > goal and j <= i:
                curr_sum -= nums[j]
                j+=1
            if curr_sum == goal:
                max_len = max(max_len,i-j+1)
                
        return -1 if max_len == -1 else len(nums) - max_len

# Question Link 
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = 0
        s = set(nums)
        
        for num in nums :
            if num-1  not in s  :
                curr_streak = 1
                nxt = num+1
                while nxt in s :
                    curr_streak+=1
                    nxt +=1
            
                streak = max(streak,curr_streak)
        return streak
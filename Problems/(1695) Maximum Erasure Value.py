# Question Link
# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # O(n) Time O(n) Space
        curr_score = 0
        max_score = 0 
        i = j = 0
        s = set()
        
        while j< len(nums) :
            if nums[j] in s:
                s.remove(nums[i])
                curr_score-= nums[i]
                i+=1

            else:

                s.add(nums[j])
                curr_score+= nums[j]
                j+=1
            max_score = max(max_score,curr_score)
        return max_score
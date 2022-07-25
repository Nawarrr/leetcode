# Question Link
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/submissions/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        pairs = 0
        left = 0
        for key in counter.keys():
            pairs += counter[key] // 2
            left+= counter[key] % 2
        
        return [pairs,left]
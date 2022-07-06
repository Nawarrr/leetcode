# Question Link
# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diffs = [nums[i] - nums[i-1] for i in range(1,len(nums)) if (nums[i] - nums[i-1]) !=0 ]
        if not diffs:  return 1
        count = 2

        for i in range(1,len(diffs)):
            if (diffs[i-1] <0 and diffs[i] >0 ) or (diffs[i-1] >0 and diffs[i] <0 ) :
                count+=1
        return count
                    
# Question Link
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # O(n) Time 
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
                continue
            i+=1
# Question Link
# https://leetcode.com/problems/remove-element/

class Solution:
    # O(n) Time
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            i+=1
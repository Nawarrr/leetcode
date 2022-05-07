# Question Link
# https://leetcode.com/problems/132-pattern/

class Solution:
    # O(n) O(n)
    def find132pattern(self, nums: List[int]) -> bool:
        
        stack = []
        three = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < three :
                return True
            while stack and stack[-1] <nums[i]:
                three = stack.pop()
            stack.append(nums[i])
        return False
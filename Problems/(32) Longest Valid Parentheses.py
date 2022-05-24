# Question Link
# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    # O(n) Time O(1) Space
    def longestValidParentheses(self, s: str) -> int:
        # from start
        left = 0
        right = 0
        max_len = 0
        for c in s :
            if c == "(":
                left +=1
            else :
                right+=1
            if right == left:
                max_len = max(max_len , left*2)
            elif right > left :
                left = 0
                right = 0
        
        # from end 
        left = 0
        right = 0
        reversed_s = s[::-1]
        for c in  reversed_s :
            if c == "(":
                left +=1
            else :
                right+=1
            if right == left:
                max_len = max(max_len , left*2)
            elif right < left :
                left = 0
                right = 0
            
            
        return max_len


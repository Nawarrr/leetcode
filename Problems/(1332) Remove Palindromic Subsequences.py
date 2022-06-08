# Question Link
# https://leetcode.com/problems/remove-palindromic-subsequences/



class Solution:
    # O(n) Time O(1) Space
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
    

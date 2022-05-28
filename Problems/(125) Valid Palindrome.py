# Question Link
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    # O(n) Time O(1) Space
    def isPalindrome(self, s: str) -> bool:
        s = "".join(e for e in s if e.isalnum())
        
        
        
        if s.lower() == s[::-1].lower():
            return True
        else:
            return False
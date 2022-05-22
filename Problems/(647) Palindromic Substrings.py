# Question Link
# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    # O(n^2) Time O(1) Space
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for x in range(len(s)):
            # Odd Palindromes
            i,j = x,x
            while 0<=i<n  and 0<=j<n and  s[i] == s[j]:
                count+=1
                i-=1
                j+=1
            # Even Palindromes
            i,j = x,x+1
            while 0<=i<n  and 0<=j<n and  s[i] == s[j]:
                count+=1
                i-=1
                j+=1
        return count   
        
        
        
        
        
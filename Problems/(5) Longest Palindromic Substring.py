# Question Link
# https://leetcode.com/problems/longest-palindromic-substring/

# Description
'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        
        for x in range(len(s)):
            # odd case
            i = j = x
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i+1) > len(output):
                    output = s[i:j+1]
                i-=1
                j+=1
            
            # Even case
            i , j = x , x+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i+1) > len(output):
                    output = s[i:j+1]
                i-=1
                j+=1
                
        return output

                
        


            
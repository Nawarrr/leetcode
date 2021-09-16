# Question Link
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Description 
'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                for x in range(i , start-1 , -1):
                    output += s[x]
            
                start = i+1
            if i == len(s) -1:
                output += " "
                for x in range(i , start-1 , -1):
                    output += s[x]
                    
        return output[1:]
                    
                       
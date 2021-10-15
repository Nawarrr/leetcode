# Question Link
# https://leetcode.com/problems/backspace-string-compare/

# Description
'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:


        def backspace(s,newS):
            skip = 0
            n = len(s)
            for i in range(n-1,-1,-1):
                if s[i] == "#":
                    skip +=1
                elif skip !=0:
                    skip -=1
                else:
                    newS += s[i]
            return newS
        return backspace(s,'') == backspace(t, '')
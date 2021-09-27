# Question Link
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Description
'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        sL = list(s) # Dealing with a string that you want to delete from is irritating, Edge Case : want to delete first element without knowing it's the 1st 
        for i in range(len(sL)):
            if sL[i] not in ["(" , ")"]:
                continue
            elif sL[i] == "(" :
                stack.append(i)
            else:
                if stack :
                    stack.pop()
                else:
                    sL[i] = ""
        while stack:
            sL[stack[-1]] = ""
            stack.pop()
        return "".join(sL)
                
        
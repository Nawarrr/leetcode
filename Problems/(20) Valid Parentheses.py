# Question Link
# https://leetcode.com/problems/valid-parentheses/

# Description
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1- Open brackets must be closed by the same type of brackets.
2- Open brackets must be closed in the correct order.
'''



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['[' , '{' , '('] :
                stack.append(i)
            elif stack :
                if i == ']' and stack[-1] == '[':
                    stack.pop()
                
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack
# Question Link
# https://leetcode.com/problems/remove-outermost-parentheses/


class Solution:
    # O(n) O(n)
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        output_string = ''
        i = 1 
        while i < len(s):
            if s[i] == ')' and not stack :
                i+=2
                continue
            if s[i] == "(" :
                stack.append(s[i])
            else:
                stack.pop()
            output_string += s[i]
            i+=1
        return output_string
        
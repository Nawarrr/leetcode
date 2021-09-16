# Question Link
# https://leetcode.com/problems/reverse-string/


# Description
'''
Write a function that reverses a string. The input string is given as an array of characters s.
'''


class Solution:
    # -----------------------------  O(n) Time O(1) Space ---------------------- #
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        while start < end :
            s[start] , s[end] = s[end] , s[start]
            start +=1
            end -=1
        
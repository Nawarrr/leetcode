#Quiestion link
#https://leetcode.com/problems/palindrome-number/

#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
#For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #We change x to a string
        str_x = str(x)
        # we compare string x to string x reversed :- reverisng string x using [::-1]
        return str_x ==  str_x[::-1]

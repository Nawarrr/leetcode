# Question Link
# https://leetcode.com/problems/multiply-strings/

# Description
'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        i = len(num1)-1
        j = len(num2)-1
        factor = 1

        n1 = 0
        n2 = 0
        while i >= 0:
            n1+= (ord(num1[i]) -48)*factor
           
            factor*=10
            i-=1
        factor = 1
        while j >=0:
            n2+= (ord(num2[j]) -48 )*factor
            factor*=10
            j-=1

        return str(n1*n2)



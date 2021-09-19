# Question Link
# https://leetcode.com/problems/add-strings/

# Description
'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''

class Solution:
    
    def addStrings(self, num1: str, num2: str) -> str:
        output = ""
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        while i >=0 or j >=0:
            dig1,dig2 = 0 , 0
            if i >=0:
                dig1 = ord(num1[i]) - 48
                i-=1
            if j >=0 :
                dig2 = ord(num2[j]) - 48
                j-=1
                
            sum = dig1+dig2 + carry
            if sum >9:
                carry =1
            else:
                carry = 0
            output += str(sum % 10)
        if carry > 0 :
            output +=str(carry)


        output = output[::-1]
        return  output
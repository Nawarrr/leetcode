#Question link
#https://leetcode.com/problems/reverse-integer/

#Given a signed 32-bit integer x, return x with its digits reversed.
#If reversing x causes the value to go outside
#the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 :
            x_string = str(x)[1:]
            rev_x = x_string[::-1]
            x_int = -int(rev_x)
        else:
            x_string = str(x)
            rev_x = x_string[::-1]
            x_int = int(rev_x)
        if x_int <= (-2**31) or x_int >= (2**31 -1) :
            print("yes")
            return 0
        else:
            print("no")
            return x_int

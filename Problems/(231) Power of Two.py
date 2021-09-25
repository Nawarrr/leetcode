# Question Link
# https://leetcode.com/problems/power-of-two/

# Decription
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        return n & n-1 == 0 and n > 0

# Ex 1 ----> 8
# 1000 ^ 7
# 1000 ^ 0111 = 0000
# Ex 2 -----> 9
# 1001 ^ 1000 == 0001

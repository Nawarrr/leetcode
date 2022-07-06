# Question Link
# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        
        lookup = {}
        def fibn(n):
            if n == 0 or n == 1 : return n
            if n in lookup: return lookup[n]
            lookup[n] = fibn(n-1) + fibn(n-2)
            return fibn(n-1) + fibn(n-2)
        return fibn(n)
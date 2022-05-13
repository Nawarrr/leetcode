# Question Link
# https://leetcode.com/problems/power-of-three/



from math import log10
class Solution:
    # I don't know what is the cost of that
    # O(1) Space
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        return (log10(n) / log10(3)) % 1 == 0
# Question Link
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/  
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # O(n) Time O(2**K) Space
        lookup = {}
        for i in range(len(s)-k+1):
            lookup[s[i:i+k]] = True
        return len(lookup.keys()) == 2**k
            
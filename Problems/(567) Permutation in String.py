# Question Link
# https://leetcode.com/problems/permutation-in-string/

# Decription
'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        i = 0
        j = n
        
        s1_hash = Counter(s1)
        while j <= len(s2):
            if s1_hash == Counter(s2[i:j]):
                return True
            else:
                i+=1
                j+=1
        return False

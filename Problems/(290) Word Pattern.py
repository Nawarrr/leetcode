# Question Link
# https://leetcode.com/problems/word-pattern/

# Description
'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split()
        hash = {}
        if len(pattern) != len(list_s):
            return False
        for i in range(len(pattern)):
            if hash.get(pattern[i]):
                if hash.get(pattern[i]) != list_s[i]:
                    return False
            else:
                hash[pattern[i]] = list_s[i]
        
        if len(set(hash.values())) != len(list(hash.values())):
            return False
        return True
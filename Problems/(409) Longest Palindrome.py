# Question Link
# https://leetcode.com/problems/longest-palindrome/


# Description
'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        counter = Counter(s)
        for key in counter:
            while counter[key] >= 2:
                count +=2
                counter[key] -=2
        for key in counter:
            if counter[key] == 1:
                return count+1
        return count
            
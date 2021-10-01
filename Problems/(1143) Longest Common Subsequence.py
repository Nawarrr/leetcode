# Question Link
# https://leetcode.com/problems/longest-common-subsequence/

# Description
'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    - For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1) , len(text2)
        dp = [[0 for _ in range(m+1)]for _ in range(n+1) ]
        
        for r in range(1,n+1):
            for c in range(1,m+1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c] , dp[r][c-1])
        return dp[-1][-1]
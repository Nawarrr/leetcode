# Question Link
# https://leetcode.com/problems/first-unique-character-in-a-string/


# Description
'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''







class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in range(len(s)):
            if dict.get(s[i]):
                dict[s[i]][0] +=1
            else:
                dict[s[i]] = [1,i]
        for x in s:
            if dict[x][0] == 1:
                return dict[x][1]
        
        return -1
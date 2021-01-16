#Question link
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Given a string s, find the length of the longest substring without
#repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count = 0
        ns = ""
        for i in s:
            if i not in ns:
                ns = ns + i
                count += 1
            else:
                break


        return max(count, self.lengthOfLongestSubstring(s[1:]))     

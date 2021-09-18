#Question link
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

#Given a string s, find the length of the longest substring without
#repeating characters.

class Solution:
    # -------------------------------- Recursive Approach ------------------------------ #
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
    # --------------------------------- Iterative Approach ------------------------------------#  USE THIS
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = ""
        maxLen = 0
        for i in s :
            if i not in string:
                string += i
            else:
                maxLen = max(maxLen , len(string))
                string = string[string.index(i)+1:] + i
            
        maxLen = max(maxLen , len(string))
        return maxLen
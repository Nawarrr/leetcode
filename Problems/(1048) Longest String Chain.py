# Question Link 
# https://leetcode.com/problems/longest-string-chain/


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        s = set(words)
        lookup = {}
        
        def count(word):
            if word not in s : return 0
            
            if word in lookup: return lookup[word] 
            
            mx = 0
            for i in range(len(word)):
                mx = max(mx, 1+ count(word[0:i] + word[i+1:]))
            lookup[word] = mx
            return mx
        
        for word in words:
            count(word)
        return max(lookup.values())
        
        
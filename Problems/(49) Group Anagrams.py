# Question Link
# https://leetcode.com/problems/group-anagrams/


# Description
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            hash[sorted_word].append(word)
            
        return hash.values()
        
                        
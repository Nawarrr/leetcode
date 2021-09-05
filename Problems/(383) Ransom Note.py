# Question Link
# https://leetcode.com/problems/ransom-note/

#Description
'''
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
# ------------------------------- O(M) Soultion -----------------------------#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        mag_hash = {}
        for i in magazine:
            if mag_hash.get(i):
                mag_hash[i] +=1
            else:
                mag_hash[i] = 1
        for letter in ransomNote:
            if mag_hash.get(letter) :
                mag_hash[letter] -=1
                
            else:
                return False
            
        return True
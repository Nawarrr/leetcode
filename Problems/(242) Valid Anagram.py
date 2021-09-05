# Question Link
# https://leetcode.com/study-plan/data-structure/?progress=7qztpm

# Description 
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''
class Solution:
    #-------------------------------------------------- O(n+m)--------------------------------------------------#
    def isAnagram(self, s: str, t: str) -> bool:

        s_hash = {}
        for i in s :
            if s_hash.get(i):
                s_hash[i] += 1
            else:
                s_hash[i] = 1
                

        for i in t :
            if s_hash.get(i):
                s_hash[i] -= 1
            else:
                print(i)
                print('here')
                return False
            
        for value in s_hash.values():
            if value != 0 :
                return False
        
        return True


    #-------------------------------------------------- Another soultion same complexity--------------------------------------------------#
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)== Counter(t)
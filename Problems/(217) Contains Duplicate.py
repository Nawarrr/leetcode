# Question Link
# https://leetcode.com/problems/contains-duplicate/

# Description
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums :
            if hash.get(str(i)):
                return True
            else:
                hash[str(i)] = True
        
        
        
# -------------- COULD be done using set() easily, but I was Practing Hashing from the begging -----------------#
#  set(array) and compare it's length to the array itself
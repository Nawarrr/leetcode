# Question Link
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Description
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        m = len(s)
        counterP = Counter(p)
        counterSW = Counter(s[:n])
        output = []
        print(counterP)
        for i in range(n , m+1):
            if counterSW == counterP :
                output.append(i-n)
            if i == m : # This is A really bad fix, Don't do this at home,school or Anywhere
                break
            counterSW[s[i]] += 1
            counterSW[s[i-n]] -= 1
            if counterSW[s[i-n]] == 0:
                counterSW.pop(s[i-n])

        return output
        
                
                
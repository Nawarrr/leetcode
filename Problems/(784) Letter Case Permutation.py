# Question Link
# https://leetcode.com/problems/letter-case-permutation/

# Description 
'''
Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.
'''

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = []
        def backtrack(start, current):
            if len(current) == len(s):
                output.append(current)
                return
            for i in range(start , len(s)):
                if not s[i].isalpha():
                    backtrack(i+1 ,current+s[i] )
                else:
                    backtrack(i+1 ,current+s[i].lower())
                    backtrack(i+1 ,current+s[i].upper())
        backtrack(0 , "")
        return output
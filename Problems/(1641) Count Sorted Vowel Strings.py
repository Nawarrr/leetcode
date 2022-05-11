# Question Link
# https://leetcode.com/problems/count-sorted-vowel-strings/


from math import factorial
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Use Combination with repetition, (r+n-1)C(r)  : on our case n = 5 and r = n
        return factorial(n+5-1)//(factorial(n)*factorial(5-1))
            
        
        
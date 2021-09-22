# Question Link
# https://leetcode.com/problems/repeated-dna-sequences/

# Description
'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

- For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i = 0
        j = 10
        hash = {}
        while j <= len(s):
            if hash.get(s[i:j]):
                hash[s[i:j]] += 1
            else:
                hash[s[i:j]] = 1
            i+=1
            j+=1
        output = []
        for key,value in hash.items():
            if value > 1:
                output.append(key)
                
        return output
        
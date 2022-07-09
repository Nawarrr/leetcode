# Question Link
# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        lst_s = s.split()
        lst_sorteds =  ["-" for _ in range(len(lst_s))]
        
        for word in lst_s:

            lst_sorteds[int(word[-1])-1] = word[:-1]
        
        return " ".join(lst_sorteds)
            
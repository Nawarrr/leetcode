# Question Link
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    # O(n) , O(27)=O(1) Space
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = string.ascii_uppercase
        dic = dict()

        for i in range(len(alpha)):
            dic[alpha[i]] = i+1
        
        power = 26**0
        number = 0
        for i in range(len(columnTitle)-1,-1,-1):
            number += dic[columnTitle[i]]*power
            power*=26
        return number
            
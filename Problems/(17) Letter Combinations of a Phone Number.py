# Question Link
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = [""]
        map = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        if not digits : return []
        
        for digit in digits:
            tmp = []
            for char in map[int(digit)-2]:
                for perm in output:
                    tmp.append(perm+char)
            output = tmp
        return output
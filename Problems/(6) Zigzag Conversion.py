# Question Link
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    # O(n) Time O(numRows*n)
    def convert(self, s: str, numRows: int) -> str:
        str_lst = ["" for _ in range(numRows)]
        
        i = 0
        
        while i < len(s):
            for j in range(numRows):
                str_lst[j]+= s[i]
                i+=1
                if i >= len(s):
                    return "".join(str_lst)
            for j in range(numRows-2,0,-1):
                str_lst[j] += s[i]
                i+=1
                if i >= len(s):
                    return "".join(str_lst)
        return "".join(str_lst)
                

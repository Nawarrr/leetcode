# Question Link
# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss = [0 for _ in range(len(indices))]
        
        for i in range(len(indices)):
            ss[indices[i]]= s[i]
        return "".join(ss)
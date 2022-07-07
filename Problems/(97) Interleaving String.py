# Question Link
# https://leetcode.com/problems/interleaving-string/

class Solution:
    # O(M*N) time and Space
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lookup = {}
        def interleave(s1,s2,s3):
            if (not s3) and (not s2) and (not s1): return True
            if not s3 : 
                return False
            if (not s1 or s1[0] != s3[0]) and (not s2 or s2[0] != s3[0]):
                return False
            s1_path,s2_path = False,False
            if s1 and s1[0] == s3[0]:
                s1_path = interleave(s1[1::],s2,s3[1::])
            if s2 and s2[0] == s3[0]:
                s2_path = interleave(s1,s2[1::],s3[1::])
            
            return s1_path or s2_path
        
        return interleave(s1,s2,s3)
            
            
                
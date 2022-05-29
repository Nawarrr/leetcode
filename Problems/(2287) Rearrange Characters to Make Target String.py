# Question Link
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution:
    # O(n) O(1) 
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = Counter(s)
        
        count = 0
        while True:
            for i in target:
                if not counter[i]:
                    return count
                counter[i]-=1
            count+=1
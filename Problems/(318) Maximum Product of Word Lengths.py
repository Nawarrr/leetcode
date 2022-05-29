# Question Link
# https://leetcode.com/problems/maximum-product-of-word-lengths/


class Solution:
    # Time O(N**2) -------> Checking if they itesect runs on Constant time O(26).
    # Space O(n)
    def maxProduct(self, words: List[str]) -> int:
        
        charset = [set(word) for word in words]
        
        
        maxi = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not (charset[i]& charset[j]):
                    maxi = max(maxi,(len(words[i])* len(words[j])))
        return maxi
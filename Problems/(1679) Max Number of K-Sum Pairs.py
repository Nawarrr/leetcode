# Question Link
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    # O(n) Time , O(n) Space 
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        pairs_dict = dict()
        for num in nums:
            if pairs_dict.get(k-num):
                counter+=1
                pairs_dict[k-num] -= 1 
            else:
                if pairs_dict.get(num):
                    pairs_dict[num] += 1
                else:
                    pairs_dict[num] = 1
        return counter
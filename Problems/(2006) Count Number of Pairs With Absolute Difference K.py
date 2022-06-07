# Question Link
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/submissions/


class Solution:
    # O(n) Time and O(n) Space
    def countKDifference(self, nums: List[int], k: int) -> int:


        lookup = Counter(nums)

        counter = 0

        for i in lookup :
            if lookup.get(i+k):
                counter+= lookup[i]*lookup[i+k]



        return counter
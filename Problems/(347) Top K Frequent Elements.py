# Question Link
# https://leetcode.com/problems/top-k-frequent-elements/

# Description
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = [(-v,k) for k,v in counter.items()]
        heapq.heapify(heap)
        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
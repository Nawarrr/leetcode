# Question Link
# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Description

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
# ---------------------------------- Using Heap ------------------------------------ #
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = k
        heap = []
        
        for i in nums:
            heapq.heappush(heap,i)
            if size < len(heap):
                heapq.heappop(heap)
        
        return heapq.heappop(heap)
# ------------------------------------ Quick Select --------------------------------- # 
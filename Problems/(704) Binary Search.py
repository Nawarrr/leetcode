# Question Link
# https://leetcode.com/problems/binary-search/

# Description
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''



class Solution:
    #------------- Iterative Approach -------------------#
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1
        while high >= low :
            mid = (low + high) //2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid +1
            elif target < nums[mid]:
                high = mid -1
        return -1
    #------------- Recursive Approach -------------------#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BinarySearch(arr , low , high , target):
            if low > high :
                return -1
            else: 
                mid = (low+high )//2
                if target == arr[mid] :
                    return mid
                elif arr[mid] < target :

                    return BinarySearch(arr , mid+1 , high,target)
                else:
                    return BinarySearch(arr , low , mid-1 , target)

        return BinarySearch(nums , 0 , len(nums)-1 , target)

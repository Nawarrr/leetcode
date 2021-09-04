# Question Link
# https://leetcode.com/problems/merge-sorted-array/

#Descryption
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''





class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lastElement =  n + m -1
        i = m-1
        j = n-1
        while lastElement != -1  :
            if j ==-1 :
                break
            elif nums1[i] < nums2[j] or i == -1:
                nums1[lastElement] = nums2[j]
                j -=1
                lastElement -=1
            else:
                nums1[lastElement] = nums1[i]
                i -=1
                lastElement -=1

# O(m + n) with no extra space
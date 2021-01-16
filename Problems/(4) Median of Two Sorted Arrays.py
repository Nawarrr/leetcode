#Question link
# https://leetcode.com/problems/median-of-two-sorted-arrays/

#Given two sorted arrays nums1 and nums2 of size m and n respectively,
#return the median of the two sorted arrays.

#Follow up: The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0
        r = 0
        array = []
        len1 = len(nums1)
        len2 = len(nums2)
        while not len(array) > ((len1 + len2)/2):
            if l >= len1 :
                array.append(nums2[r])
                r += 1
            elif r >= len2 :
                array.append(nums1[l])
                l +=1
            elif nums1[l] <= nums2[r]:
                array.append(nums1[l])
                l +=1
            else:
                array.append(nums2[r])
                r += 1
        print(array)
        if (len1 + len2) % 2 == 0 :
            return (array[-1] + array[-2]) /2
        else:
            return array[-1]

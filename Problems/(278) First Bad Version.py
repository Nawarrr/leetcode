# Question Link
# https://leetcode.com/problems/first-bad-version/


# Description 
'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low = 0
        high = n
        while high >= low :
            mid = (low+high) // 2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            if isBadVersion(mid):
                high = mid -1
            elif not isBadVersion(mid):
                low = mid +1
        
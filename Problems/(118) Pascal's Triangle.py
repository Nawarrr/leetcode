# Question Link
# https://leetcode.com/problems/pascals-triangle/


# Description
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it 
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTriangle = [[ 1 for _ in range(x+1) ] for x in range(numRows)]

        for rowIndex in range(1 ,numRows) :

            for index in range(1,rowIndex):
                pascalTriangle[rowIndex][index] = pascalTriangle[rowIndex-1][index-1] + pascalTriangle[rowIndex-1][index]
        return pascalTriangle


# O(n^2)
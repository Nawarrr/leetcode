# Question Link
# https://leetcode.com/problems/pascals-triangle-ii/

# Description
'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalTriangle = [[1]]
        for i in range(1,rowIndex +1 ):
            temp = [1 for i in range(i+1)]
            for j in range(1,len(temp)-1):
                temp[j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j]
            pascalTriangle.append(temp)
        return pascalTriangle[-1]
        
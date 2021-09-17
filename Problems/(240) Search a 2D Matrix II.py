# Question Link
# https://leetcode.com/problems/search-a-2d-matrix-ii/


# Description
'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = 0
        row = len(matrix)-1
        while col < len(matrix[0]) and row >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                row -=1
            else:
                col+=1
        return False
                
            
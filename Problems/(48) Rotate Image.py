# Question Link
# https://leetcode.com/problems/rotate-image/


# Description
'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

# Transpose Then Reverse For Rotation
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose The Matrix
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col] , matrix[col][row] = matrix[col][row] , matrix[row][col]

        # Reverse Every Row
        for row in matrix:
            row.reverse()
        
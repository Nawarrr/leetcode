# Question Link
# https://leetcode.com/problems/reshape-the-matrix/

#Description
'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''








class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        num_of_elements = len(mat)*len(mat[0])
# 0s Matrix with the new size
        new_mat = [[0 for i in range(c)] for j in range(r)]
# Checking Validity        
        if r*c != num_of_elements:
            return mat
        
# Getting the whole matrix in 1 array (row traversal)
        numbers = []
        for row in mat :
            numbers += row
            
        counter = 0
# Filling the new matrix
        for i in range(r):
            for j in range(c):
                new_mat[i][j] = numbers[counter]
                counter+=1
        return new_mat
                
                
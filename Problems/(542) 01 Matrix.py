# Question Link
# https://leetcode.com/problems/01-matrix/

# Description
'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])
        # Top and Left 
        for i in range(rows) :
            for j in range(cols):
                if mat[i][j] != 0:
                    if i > 0 :
                        top = mat[i-1][j]
                    else:
                        top = float('inf')
                    if j > 0:
                        left = mat[i][j-1]
                    else:
                        left = float('inf')
                    mat[i][j] = 1 + min(top,left)

        
        for i in range(rows -1 , -1 , -1):
            for j in range(cols-1 , -1 , -1):
                if mat[i][j] != 0:
                    if i < rows-1 :
                        bot = mat[i+1][j]
                    else:
                        bot = float('inf')
                    if j < cols - 1:
                        right = mat[i][j+1]
                    else:
                        right = float('inf')
                    mat[i][j] = min(1 + min(bot , right) , mat[i][j])
                    
        return mat

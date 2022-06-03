# Question Link
# https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:
    # O(M*N) first time, O(M) every other time 
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = [[0 for _ in range(len(matrix[0])+1)] for _  in range(len(matrix)+1)]
        
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.prefix_matrix[i][j] = self.prefix_matrix[i][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ = 0
        for i in range(row1+1,row2+2):
            summ+= self.prefix_matrix[i][col2+1] - self.prefix_matrix[i][col1]
        return summ
            
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
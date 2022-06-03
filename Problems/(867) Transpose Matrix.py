# Question Link
# https://leetcode.com/problems/transpose-matrix/


class Solution:
    # O(M*N)
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        new_matrix = [[0 for _ in range(len(matrix))]for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix
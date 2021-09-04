# Question Link
# https://leetcode.com/problems/search-a-2d-matrix/submissions/


# Description Link
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''






class Solution:
    # ----------------------------- O(N) Soultion ------------ Credits to Salman ------------------#
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) -1
        col = 0
        
        while row >=0 and col < len(matrix[0]):
            if target > matrix[row][col]:
                col+=1
            elif target<matrix[row][col]:
                row -=1
            elif target == matrix[row][col]:
                return True
                
        return False


    # ---------------------------- Log(M+N) Soultion -----------------------#
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) 
        n = len(matrix[0])
        
        low = 0
        high = m*n -1
        while low <= high:
            mid = (low+high) //2
            mid_row,mid_col = divmod(mid , n)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                low = mid+1
            else:
                high = mid -1
        return False
    
    
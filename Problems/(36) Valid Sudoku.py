# Question Link
# https://leetcode.com/problems/valid-sudoku/

# Description 
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking Row
        for row in board :
            row_dict = {}

            for i in row:
                if i != '.':
                    if row_dict.get(i):
                        print('row')
                        return False
                    else:
                        row_dict[i] = True
        # Checking Column
        for i in range(0,9):
            col_dict = {} 
            for row in board:
                if row[i] != '.' :
                    if col_dict.get(row[i]):
                        print('col')
                        return False
                    else:
                        col_dict[row[i]] = True
        # Checking Square
        
        for k in range(0,3):
            for m in range(0,3):
                sq_hash = {}
                for i in range(3*k , (3*k)+3):
                    for j in range(3*m,(3*m)+3):
                        if board[i][j] != '.':
                            if sq_hash.get(board[i][j]):
                                return False
                            else:
                                sq_hash[board[i][j]] = True



            
        return True

        

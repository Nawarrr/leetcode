# Question Link
# https://leetcode.com/problems/word-search/

# Description
'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        firstLetter = word[0]
        fristLetterIndecies = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == firstLetter:
                    fristLetterIndecies.append((row,col))
                    
        def dfs(i,j,word):
            if len(word) == 0:
                return True
            if i< 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j] == None:
                return False
            
            if board[i][j] == word[0]:
                temp = visited[i][j]
                visited[i][j] = None
                if dfs(i+1,j,word[1::]) or dfs(i-1,j,word[1::]) or dfs(i,j+1,word[1::]) or dfs(i,j-1,word[1::]):
                    return True
                visited[i][j] = temp
            
            
            
        visited = copy.deepcopy(board)
        for row,col in fristLetterIndecies:
            if dfs(row,col,word):
                return True
        return False
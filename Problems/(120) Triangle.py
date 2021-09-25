# Question Link
# Description

# Description
'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
'''

class Solution:
    # ------------------------------------------------------- O(n**2)  O(n*2) space ----------------------------# 
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        output = [[0 for _ in range(i+1) ]  for i in range(len(triangle))]
        output[0][0] = triangle[0][0]
        
        for i in range(1,len(triangle)):
            output[i][0] = output[i-1][0] + triangle[i][0]
            output[i][-1] = output[i-1][-1] + triangle[i][-1]
            for j in range(1,len(triangle[i])-1):
                output[i][j] = triangle[i][j] + min(output[i-1][j-1] , output[i-1][j])

        return min(output[-1]) 
    

    # ------------------------------------------------------- O(n**2)  O(n) space ----------------------------# 
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        
        
        
        for i in range(len(triangle)-2 , -1 , -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j] ,triangle[i+1][j+1])
        print(triangle)
        return triangle[0][0]
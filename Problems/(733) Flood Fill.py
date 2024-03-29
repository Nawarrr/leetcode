# Question Link
# https://leetcode.com/problems/flood-fill/


# Description
'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        def dfs(i , j ):
            
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != oldColor or  image[i][j] == newColor:
                return 
            
            image[i][j] = newColor
            dfs(i+1 ,j)
            dfs(i-1 ,j)
            dfs(i ,j+1)
            dfs(i ,j-1)
            
        dfs(sr,sc)
        return image
#Question link
#https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
#You are given an array rectangles where
#rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

#You can cut the ith rectangle to form a square with
#a side length of k if both k <= li and k <= wi. For example,
# if you have a rectangle [4,6],
#you can cut it to get a square with a side length of at most 4.

#Let maxLen be the side length of the largest square you can obtain
#from any of the given rectangles.

#Return the number of rectangles that can make a square with a side length of maxLen.

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        #Initializing maxLen and counter with 0
        maxLen = 0
        count = 0
        # looping to find the biggest minimum of the rectangles
        for i in rectangles:
            if min(i) > maxLen:
                maxLen = min(i)
        #looping to find how many rectangles have that minimum so we can form squares from them
        for i in rectangles:
            if min(i) == maxLen:
                count +=1
        #returning the counter
        return count

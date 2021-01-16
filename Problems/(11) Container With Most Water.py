#Question link
#https://leetcode.com/problems/container-with-most-water/

#Given n non-negative integers a1, a2, ..., an ,
#where each represents a point at coordinate (i, ai).
#n vertical lines are drawn such that the two endpoints of the line i is at (i, ai)
#and (i, 0). Find two lines, which, together with the x-axis forms a container,
#such that the container contains the most water.

#Notice that you may not slant the container.


#BRUTE FORCE SOULTION
#TIME LIMIT EXCEEDED USING PYTHON


#class Solution:

#    def maxArea(self, height: List[int]) -> int:
#        #Initializing and Empty List
#        list_of_areas = []
#        #looping on the list of heights with i as the index of the element
#        for i in range(0 , len(height)):
#            #looping on the list of heights from the element with index i+1
#
#            for j in range((i+1),len(height)):
#                #We calculate the are by determining the min height and multiplying
#                #it by the diff between indicies (length)
#                area = min(height[i],height[j]) *( j-i )
#                #appending the result to a list
#                list_of_areas.append(area)
#
#        # We return the maximum value
#        return max(list_of_areas)

#EFFICIENT SOULTION
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #initializing pointers on the begging and end of the list
        i = 0
        l = len(height) -1
        max_area = 0
        #check for max area untill the 2 pointer points to the same point (all the cases got covered)
        while i != l:
            #Calculating the new_area = Length * height while length is the index
            new_area = ((l-i) * min(height[i] , height[l]))
            #Checking if the new area is bigger than the old one
            if  new_area > max_area:
                max_area = new_area

            if height[i] <= height[l]:
                i += 1
            else:
                l -= 1
        # Returning the maximum area
        return max_area

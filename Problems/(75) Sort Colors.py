# Question Link
# https://leetcode.com/problems/sort-colors/submissions/


# Description
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ----------------------- O(n) Two Path Soultion ------------------------#
        count_zero = 0
        count_one = 0
        count_two = 0
        for i in nums: 
            if i == 0: count_zero+=1
            elif i == 1: count_one+=1
            else: count_two+=1
        for i in range(len(nums)): # O(n)
            if count_zero:
                nums[i] = 0
                count_zero -=1
            elif count_one:
                nums[i] = 1
                count_one -=1
            else:
                nums[i] = 2
                count_two -=1

    # ----------------------- O(n) One Path Soultion ------------------------#
        # Dutch Flag Algorithm # 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red,white, blue = 0 , 0 , len(nums)-1
        while white <= blue :
            if nums[white] == 0:
                nums[white] , nums[red] = nums[red] , nums[white]
                white +=1
                red +=1
            elif  nums[white] == 1:
                white +=1
            else:
                nums[white] , nums[blue] = nums[blue] , nums[white]
                blue -=1
            
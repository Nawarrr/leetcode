# Question Link
# https://leetcode.com/problems/product-of-array-except-self/

# Description
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution:
    # -------------------- O(n) O(n) ------------------------#
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrFromLeft = [1]
        arrFromRight = [1]
        product = 1
        output = []
        for i in range(1,len(nums)):
            product *= nums[i-1] 
            arrFromLeft.append(product)
        product = 1
        for i in range(1,len(nums)):
            product *= nums[-i] 
            arrFromRight.append(product)
        arrFromRight.reverse()
        print(arrFromRight , arrFromLeft)
        for i in range(len(nums)):
            output.append(arrFromRight[i]*arrFromLeft[i])
        return output

    # -------------------- O(n) O(1) ------------------------#
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        product = 1
        # Loop From Left to Right
        for i in range(1,len(nums)):
            product *= nums[i-1] 
            output.append(product)
        
        product = 1
        # Loop From Right to Left
        for i in range(len(nums)-1, -1 , -1):
            output[i] *=product
            product *=nums[i]
        
        return output
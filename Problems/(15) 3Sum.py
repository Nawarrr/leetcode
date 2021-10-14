# Question Link
# https://leetcode.com/problems/3sum/

# Description
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
# Hash Map Soultion

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums = sorted(nums)

        hash = {}
        for i in range(len(nums)) :
            hash = {}
            for j in range(i+1 , len(nums)) :
                if hash.get(nums[j]):
                    if len(hash[nums[j]]) == 2:
                        hash[nums[j]].append(nums[j])
                        output.append(hash[nums[j]])

                else :
                    hash[ -(nums[i] + nums[j])] = [nums[i] , nums[j]]
        set_output = set()
        for i in output:
            set_output.add(tuple(i))
        output = []
                          
        for i in set_output :
            output.append(list(i))
                          
        return output

# Two Pointer Soultion

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = set()
        for i in range(len(nums)):
            target = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -target :
                    triplet = (target , nums[j] , nums[k])
                    output.add(triplet)
                    j += 1
                elif nums[j] + nums[k] > -target:
                    k -=1
                else:
                    j += 1
                
        finalOutput = []
        for i in output:
            finalOutput.append(list(i))
        return finalOutput
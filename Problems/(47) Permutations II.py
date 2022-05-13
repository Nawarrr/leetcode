# Question Link
# https://leetcode.com/problems/permutations-ii/

class Solution:
    # Not sure about complexities 
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        counter = Counter(nums)

        def backtrack(perm,counter):
            if len(perm) == len(nums):
                output.append(perm.copy())
                return
            for num in counter:
                if counter[num] > 0:
                    perm.append(num)
                    counter[num]-=1
                    
                    backtrack(perm , counter)
                    
                    perm.pop()
                    counter[num] +=1
        
        backtrack([],counter)
        return output
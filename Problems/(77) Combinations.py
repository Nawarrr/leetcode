# Quesiton Link
# https://leetcode.com/problems/combinations/

# Description
'''
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(start , combination):
            if len(combination) == k :
                output.append(combination.copy())
                return
            for i in range(start, n+1):
                combination.append(i)
                backtrack(i+1 , combination)
                combination.pop()
        backtrack(1 , [])
        return output
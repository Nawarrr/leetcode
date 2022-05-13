# Question Link
# https://leetcode.com/problems/happy-number/

class Solution:
    # O(logn) O(logn) Check Leetcode's soultion on this question to understand why
    def isHappy(self, n: int) -> bool:
        def calculate_sum(n):
            sum = 0
            while n > 0:
                number = n%10
                n = n //10
                sum+= number**2
            return sum
        hash = {}
        sum = calculate_sum(n)
        
        while not hash.get(sum):
            if sum == 1 :
                return True
            hash[sum] = True
            sum = calculate_sum(sum)
        return False
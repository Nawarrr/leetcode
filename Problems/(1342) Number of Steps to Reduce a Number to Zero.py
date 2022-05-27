# Question Link
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    # Common Sense Solution
    def numberOfSteps(self, num: int) -> int:
        count =0
        while num >0:
            if num % 2 == 0:
                num /=2
            else:
                num-=1
            count+=1
        return count
    
    # Bit Manipulation Solution
    def numberOfSteps(self, num: int) -> int:
        if num == 0 : return 0
        count =0
        while num >0:
            if (num & 1):
                count+=2
            else:
                count+=1
            num = num >> 1
        return count-1 # Everytime we have a one, we add 2, now think about the last 1 we have 
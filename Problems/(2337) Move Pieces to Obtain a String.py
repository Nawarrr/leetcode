# Question Link
# https://leetcode.com/problems/move-pieces-to-obtain-a-string/


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if Counter(start) != Counter(target) : return False
        if start.replace("_", "") != target.replace("_", "") : return False
        lastL1 = 0
        firstR1  = 0
        for i in range(len(start)):
            if start[i] == 'L':
                lastL1 = i
        for i in range(len(start)):
            if start[i] == 'R':
                firstR1 = i
                break
        lastL2 = 0
        firstR2  = 0
        for i in range(len(target)):
            if target[i] == 'L':
                lastL2 = i
        for i in range(len(target)):
            if target[i] == 'R':
                firstR2 = i
                break

        if lastL1 < lastL2 or firstR1 > firstR2 : 
            return False
        else: 
            return True
        
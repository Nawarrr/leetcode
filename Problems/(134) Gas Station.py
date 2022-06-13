# Question Link
# https://leetcode.com/problems/gas-station/

class Solution:
    # O(n) Time O(n) Space
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        curr_gas = 0
        total_gas = 0
        position = 0
        flag = True  # Might not be the best idea but it's what I got in mind
        for i in range(len(gas)):
            curr_gas+= gas[i]
            total_gas = total_gas - cost[i] + gas[i]
            curr_gas-= cost[i]
            if curr_gas >=0 and flag  :
                position = i
                flag = False
            if curr_gas < 0:
                curr_gas = 0
                flag = True
                
        if total_gas < 0 : return -1
        return position
    

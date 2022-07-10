class Solution:
    # O(n) Time O(n) Space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_so_far = [0 for _ in range(len(cost))]
        
        cost_so_far[0] = cost[0]
        cost_so_far[1] = cost[1]
        
        for i in range(2,len(cost)):
            cost_so_far[i] = cost[i]+min(cost_so_far[i-1] , cost_so_far[i-2])
        
        return min(cost_so_far[-1] , cost_so_far[-2])
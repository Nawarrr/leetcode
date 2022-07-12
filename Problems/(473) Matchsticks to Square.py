# Question Link
# https://leetcode.com/problems/matchsticks-to-square/


class Solution:
    # O(2*N) Time O(N) Space 
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if  perimeter %4 != 0 : return False 
        side =  perimeter / 4 
        matchsticks.sort(reverse=True)
        l1 = l2 = l3 = l4 = 0
        @lru_cache
        def dfs(l1,l2,l3,l4,i):
            if i == len(matchsticks):
                if l1==l2==l3==l4:
                    return True
                else : 
                    return False
            
            ms = matchsticks[i]
            if l1+ms <= side and dfs(l1+ms,l2,l3,l4,i+1):
                return True
            if l2+ms <= side and dfs(l1,l2+ms,l3,l4,i+1):
                return True
            if l3+ms <= side and dfs(l1,l2,l3+ms,l4,i+1):
                return True
            if l4+ms <= side and dfs(l1,l2,l3,l4+ms,i+1):
                return True
            return False
        return dfs(l1,l2,l3,l4,0)
# Question Link
# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    # I really don't know how much time does that work in, But I think it's O(2^k) which is O(1) as k max value is 9
    # The Question is sketchy a little but both n and k have finite values (n max value = 60  and k max value is 9 )
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        
        def dfs(tmp,num,summ):
            if len(tmp)  == k:
                if summ == n:
                    output.append(tmp)
                return
            for i in range(num,10):
                if summ+i > n:
                    break
                
                dfs(tmp+[i],i+1,summ+i)
        dfs([],1,0)
        return output
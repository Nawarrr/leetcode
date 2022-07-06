# Question Link
# https://leetcode.com/problems/candy/


class Solution:
    def candy(self, ratings: List[int]) -> int:
        leftright = [1]
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                leftright.append(leftright[i-1]+1)
            else:
                leftright.append(1)

        rightleft = [1 for _ in range(len(ratings))]
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                rightleft[i] = rightleft[i+1]+1
            else:
                rightleft[i] = 1
        
        candies = []
        for i in range(len(ratings)):
            candies.append(max(leftright[i] , rightleft[i]))

        return sum(candies)
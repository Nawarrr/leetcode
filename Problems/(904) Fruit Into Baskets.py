# Question Link
# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    # O(n) Time and Space
    def totalFruit(self, fruits: List[int]) -> int:
        counter = {}
        start = 0
        max_friuts = 0
        for end in range(len(fruits)):
            if fruits[end] in counter :
                counter[fruits[end]]+=1
            else:
                counter[fruits[end]]=1

            while len(counter.keys()) > 2 :
                counter[fruits[start]] -=1
                if counter[fruits[start]] == 0 :
                    counter.pop(fruits[start])
                start+=1

            max_friuts = max(max_friuts ,abs(end-start)+1)
            
        return max_friuts
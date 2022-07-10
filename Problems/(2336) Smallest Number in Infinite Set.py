# Question Link
#https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.s = [i+1 for i in range(1001)]
        self.start = 0

    def popSmallest(self) -> int:
        
        val = self.s[self.start]
        self.s[self.start] = '-'
        while self.s[self.start] == '-':
            self.start +=1
        return val
        
    def addBack(self, num: int) -> None:
        if self.s[num-1] != '-':
            return
        #self.start = min(self.start , num-1)
        #self.s[self.start] = num
        self.s[num-1]  = num
        i = 0
        while True :
            if self.s[i] != '-':
                self.start = i
                break
            i+=1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
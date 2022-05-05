# Question Link
# https://leetcode.com/problems/implement-stack-using-queues/


# DECLERATION : This isn't a good soultion , doing a stack that does O(n) for top is bad implementation, a O(n) Push is way better in my opinion,
# There are alot of diffrent ways to implement this, this is a 1 queue implementation

class MyStack:

    def __init__(self):
        self.queue = []
    def push(self, x: int) -> None: # O(1)
        self.queue.append(x) 

    def pop(self) -> int: # O(n)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
        

    def top(self) -> int: # O(n)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        x = self.queue.pop(0)
        self.queue.append(x)
        return x

    def empty(self) -> bool: # O(1)
        return len(self.queue) ==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
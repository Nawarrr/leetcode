# Question Link
# https://leetcode.com/problems/min-stack/


# Description
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minHash = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) >1:
            self.minHash[len(self.stack)-1] = min(self.minHash[len(self.stack)-2] , val)
        else:
            self.minHash[0] = val

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHash[len(self.stack)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
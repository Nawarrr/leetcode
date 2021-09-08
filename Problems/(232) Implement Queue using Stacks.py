# Question Link
# https://leetcode.com/problems/implement-queue-using-stacks/

# Description
'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack  = []
        self.temp = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.stack:

            self.temp.append(self.stack.pop())
            
        lastElement = self.temp.pop()
        
        while self.temp:

            self.stack.append(self.temp.pop())
            
        return lastElement
       
            
            
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack:
            self.temp.append(self.stack.pop())
            
            
        peekElement = self.temp[-1]
        while self.temp:
            self.stack.append(self.temp.pop())
            
        return peekElement
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
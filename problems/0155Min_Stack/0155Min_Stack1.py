"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/25/2020
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = []

    def push(self, x: int) -> None:
        self.Stack.append(x)

    def pop(self) -> None:
        if self.Stack:
            self.Stack.pop()

    def top(self) -> int:
        if self.Stack:
            return self.Stack[-1]

    def getMin(self) -> int:
        temp = self.Stack
        
        if self.Stack:
            return sorted(temp)[0]
        else:
            return None


if __name__ == '__main__':
    a = MinStack()

    a.push(-2)
    a.push(0)
    a.push(-3)
    print(a.getMin())
    a.pop()
    a.top()
    print(a.getMin())



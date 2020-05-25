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
        self.min_value = []

    def push(self, x: int) -> None:
        self.Stack.append(x)

        if not self.min_value or x <= self.min_value[-1]:
            self.min_value.append(x)


    def pop(self) -> None:
        if self.Stack:
            if self.Stack[-1] == self.min_value[-1]:
                self.min_value.pop()

        self.Stack.pop()

    def top(self) -> int:
        if self.Stack:
            return self.Stack[-1]

    def getMin(self) -> int:
        if self.Stack:
            return self.min_value[-1]


if __name__ == '__main__':
    a = MinStack()

    a.push(-2)
    a.push(0)
    a.push(-3)
    print(a.getMin())
    a.pop()
    a.top()
    print(a.getMin())



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

        if not self.min_value or x < self.min_value[-1][0]:
            self.min_value.append([x, 1])
        elif x == self.min_value[-1][0]:
            self.min_value[-1][1] += 1


    def pop(self) -> None:
        if self.Stack:
            if self.Stack[-1] == self.min_value[-1][0]:
                if self.min_value[-1][1] > 1:
                    self.min_value[-1][1] -= 1
                else:
                    self.min_value.pop()

        self.Stack.pop()

    def top(self) -> int:
        if self.Stack:
            return self.Stack[-1]

    def getMin(self) -> int:
        if self.Stack:
            return self.min_value[-1][0]



if __name__ == '__main__':
    a = MinStack()

    a.push(0)
    a.push(1)
    a.push(0)
    print(a.getMin())
    a.pop()
    a.top()
    print(a.getMin())




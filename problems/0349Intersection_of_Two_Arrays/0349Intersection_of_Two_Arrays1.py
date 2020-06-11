"""

Version: 1.1 
Author:  Yanrui 
date:    06/11/2020
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def peekMax(self) -> int:
        if len(self.stack) > 0:
            return max(self.stack)

    def popMax(self) -> int:
        if len(self.stack) > 0:
            max_val = max(self.stack)
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i] == max_val:
                    return self.stack.pop(i)


if __name__ == '__main__':

    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(5)
    stack.top()
    stack.popMax()
    stack.top()
    stack.peekMax()
    stack.pop()
    stack.top()
    

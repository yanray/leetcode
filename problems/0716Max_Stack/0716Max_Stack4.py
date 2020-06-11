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
        self.maxvalue = None
        self.maxstack = []
        
    def check_empty(self):
        if self.maxstack:
            return 1
        else:
            return 0
    
    def push(self, x: int) -> None:
        self.maxstack.append(x)
        if self.maxvalue == None or x > self.maxvalue:
            self.maxvalue = x
        

    def pop(self) -> int:
        if not self.maxstack:
            return
        tmp = self.maxstack.pop()
        if self.check_empty():
            maxvalue = None
        if not self.check_empty():
            self.maxvalue = None
        if tmp == self.maxvalue and self.check_empty():
            self.maxvalue = max(self.maxstack)
        return tmp

    def top(self) -> int:
        if not self.check_empty():
            return
        return self.maxstack[-1]
        

    def peekMax(self) -> int:
        return self.maxvalue

    def popMax(self) -> int:
        if not self.check_empty():
            return
        tmp = self.maxvalue
        for i in range(len(self.maxstack)-1,-1,-1):
            if self.maxstack[i] == tmp:
                self.maxstack.pop(i)
                break
        if self.check_empty():
            self.maxvalue = max(self.maxstack)
        else:
            self.maxvalue = None
        return tmp


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
    

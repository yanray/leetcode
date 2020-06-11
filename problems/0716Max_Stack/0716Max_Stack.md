## Max Stack

### Problem Link

https://leetcode.com/problems/max-stack/

### Problem Description 

Design a max stack that supports push, pop, top, peekMax and popMax.

1. push(x) -- Push element x onto stack.
2. pop() -- Remove the element on top of the stack and return it.
3. top() -- Get the element on the top.
4. peekMax() -- Retrieve the maximum element in the stack.
5. popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

```
Example 1: 

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

```

**Note:**

1. -1e7 <= x <= 1e7
2. Number of operations won't exceed 10000.
3. The last four operations won't be called when stack is empty.

### How to solve 

**Approach 1:** 


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0716Max_Stack/0716Max_Stack1.py)

```python
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
```

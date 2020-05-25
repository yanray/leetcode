## Min Stack

### Problem Link
https://leetcode.com/problems/verifying-an-alien-dictionary/

### Problem Description 

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.

```
Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

```

### How to solve 

**Approach 1:** 

Use one list to represent Stack, get minimum values by sorting, but this is pretty slow

**Approach 2:** 

Use one stack to store pairs (x, min_value)

**Approach 3:** 

Use two Stacks, one for x, one for min_value

**Approach 4:** 

Improved two Stacks.

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0155Min_Stack/0155Min_Stack1.py)

```python
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
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0155Min_Stack/0155Min_Stack2.py)

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Stack = []

    def push(self, x: int) -> None:
        if not self.Stack:
            self.Stack.append((x, x))

        current_min = self.Stack[-1][1]
        self.Stack.append((x, min(x, current_min)))


    def pop(self) -> None:
        if self.Stack:
            self.Stack.pop()

    def top(self) -> int:
        if self.Stack:
            return self.Stack[-1][0]

    def getMin(self) -> int:
        if self.Stack:
            return self.Stack[-1][1]

```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0155Min_Stack/0155Min_Stack3.py)

```python
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
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0155Min_Stack/0155Min_Stack4.py)

```python
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
```
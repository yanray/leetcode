## Range Sum of BST

### Problem Link

https://leetcode.com/problems/range-sum-of-bst/

### Problem Description 

Implement the following operations of a queue using stacks.

* push(x) -- Push element x to the back of queue.
* pop() -- Removes the element from in front of queue.
* peek() -- Get the front element.
* empty() -- Return whether the queue is empty.


```
Example 1:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

```

**Note:**

* You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

### Code (python)

[Approach 1] (90%)

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.instack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.outstack) == 0:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.outstack) == 0:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.instack) == 0 and len(self.outstack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty() 
```

[Approach 2] (75%)

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_f = []
        self.stack_s = []
        
    def shift(self):
        """
		Shift all the elements of stack_f to stack_s
		"""
        while self.stack_f:
            self.stack_s.append(self.stack_f.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_f.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack_s) != 0:
            return self.stack_s.pop()
        self.shift()
        return self.stack_s.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack_s) == 0:
            self.shift()
        return self.stack_s[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack_f)+len(self.stack_s) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
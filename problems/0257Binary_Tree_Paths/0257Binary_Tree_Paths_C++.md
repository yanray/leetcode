## Moving Average from Data Stream

### Problem Link

https://leetcode.com/problems/moving-average-from-data-stream/

### Problem Description 

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

```
Example 1:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

```

### Code (python)

[Approach 1] (62%) 

```python
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window_size = size
        self.stack = []
        self.prev_sum = 0

    def next(self, val: int) -> float:
        
        self.stack.append(val)
        self.prev_sum += val
        
        if len(self.stack) <= self.window_size:
            return self.prev_sum / len(self.stack)
        else:
            self.prev_sum -= self.stack[-self.window_size - 1]
            return self.prev_sum / self.window_size
```

[Approach 2: Array or List]

```python
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []
        
    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)
```

[Approach 3: Double-ended Queue]  (62%) O(1)

```python
from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0
    
    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum / min(self.size, self.count)
```

[Approach 4: Circular Queue with Array] (67%) O(1)

```python
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0
    
    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
```
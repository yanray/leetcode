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


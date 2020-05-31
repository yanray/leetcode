## Missing Number

### Problem Link

https://leetcode.com/problems/missing-number/

### Problem Description 

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

```
Example 1: 

Input: [3,0,1]
Output: 2

```

```
Example 2: 

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

```

### How to solve 

**Approach 1:** 

Hashtable / Dictionary

**Approach 1:** 

Queue + Set

https://blog.csdn.net/hellojoy/article/details/81281367

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0359Logger_Rate_Limiter/0359Logger_Rate_Limiter1.py)

```python
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.log_dict:
            self.log_dict[message] = timestamp
            return True
        else:
            if timestamp - self.log_dict[message] >= 10:
                self.log_dict[message] = timestamp
                return True
            else:
                return False
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0359Logger_Rate_Limiter/0359Logger_Rate_Limiter2.py)

```python
from collections import deque

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_set = set()
        self._msg_queue = deque()
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0359Logger_Rate_Limiter/0359Logger_Rate_Limiter3.py)

```python
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log_times = dict()
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        # logging timeout in seconds
        TIMEOUT = 10
        # the following three cases are possible
        # 1) the message has not been printed before -> true
        if message not in self.log_times:
            # create a log in the hashmap
            self.log_times.update({message: timestamp})
            return True
        
        else:
            # 2) the message has been printed before and the timer has expired -> true
            if timestamp - self.log_times[message] >= TIMEOUT:
                self.log_times.update({message: timestamp})
                return True
            # 3) the message has been printed before and timer has not expired -> false
            else:
                return False
```

## Logger Rate Limiter

### Problem Link

https://leetcode.com/problems/logger-rate-limiter/

### Problem Description 

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

```
Example 1: 

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
```

**Note:** You may assume the string contain only lowercase letters.

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

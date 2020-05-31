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


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0387First_Unique_Character_in_a_String/0387First_Unique_Character_in_a_String1.py)

```python
see_once = {}
for i, ch in enumerate(s):
    if ch in see_once:
        see_once[ch] = -1
    else:
        see_once[ch] = i

for v in see_once.values():
    if v != -1:
        return v
        
return -1
```


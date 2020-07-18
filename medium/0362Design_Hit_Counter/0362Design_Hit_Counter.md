## Design Hit Counter

### Problem Link

https://leetcode.com/problems/design-hit-counter/

### Problem Description 

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

```
Example 1:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 


```

**Follow up:**

What if the number of hits per second could be very large? Does your design scale?

### Code (python)

[Approach 1] (%) 

```python
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        lower_bound = timestamp - 300
        if lower_bound > 0:
            while self.queue:
                t = self.queue[0]
                if t > lower_bound:
                    break
                else:
                    self.queue.pop(0)
            
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
```

https://leetcode.com/problems/design-hit-counter/discuss/734736/Python-List-%2B-Dictionary-%2B-Binary-Search-93-memory

https://leetcode.com/problems/design-hit-counter/discuss/572999/Easy-Solution-design-using-dict-hit-is-O(1)-and-getHits()-is-O(s)


[Approach 2]

```python
import bisect
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = [0]
        self.hits = {0 : 0}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp == self.time[-1]:
            self.hits[timestamp] += 1
        else:
            self.hits[timestamp] = self.hits[self.time[-1]] + 1
            self.time.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        pre, cur = timestamp - 300, timestamp
        i = bisect.bisect_right(self.time, pre)
        j = bisect.bisect_right(self.time, cur)
        res = 0 if j == 0 else self.hits[self.time[j - 1]]
        res -= 0 if i == 0 else self.hits[self.time[i - 1]]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
```

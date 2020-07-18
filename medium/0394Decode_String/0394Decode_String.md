## Decode String

### Problem Link

https://leetcode.com/problems/decode-string/

### Problem Description 

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

```
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

```

```
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

```

```
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

```

```
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

```


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

[Approach 3]

```python
import heapq
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.rec = []
        #heapq.heapify(self.rec)

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        heapq.heappush(self.rec, timestamp)
     

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        check = max(0, timestamp - 300)
        while self.rec and check >= self.rec[0]:
            heapq.heappop(self.rec)
        
        return len(self.rec)
```


https://leetcode.com/problems/design-hit-counter/discuss/524564/Python-Solution


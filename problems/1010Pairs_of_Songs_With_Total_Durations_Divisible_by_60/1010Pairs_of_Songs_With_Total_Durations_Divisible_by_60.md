## Pairs of Songs With Total Durations Divisible by 60

### Problem Link

https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

### Problem Description 

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

```
Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

```

```
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

```

**Note:**

* 1 <= time.length <= 60000
* 1 <= time[i] <= 500

### Code (python)

[Approach 1: Using defaultdict] (15%)

```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = 0
        hash_dict = collections.defaultdict(int)
        for i in range(len(time)):
            if time[i] % 60 in hash_dict:
                count += hash_dict[time[i] % 60]
            hash_dict[(60 - time[i]) % 60] += 1
                    
        return count 
```

[Approach 2] (87%)

```python
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        m, d = 0, collections.Counter([t%60 for t in time])
        for k in d:
            if k == 0 or k == 30:
                m += d[k]*(d[k]-1)//2
            elif k < 30 and 60-k in d:
                m += d[k]*d[60-k]
        return m
```
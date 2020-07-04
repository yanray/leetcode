## Implement strStr()

### Problem Link

https://leetcode.com/problems/implement-strstr/

### Problem Description 

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

```
Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

```

```
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

```

**Clarification:**

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


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
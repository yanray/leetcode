## Fibonacci Number

### Problem Link

https://leetcode.com/problems/fibonacci-number/

### Problem Description 

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 

That is,
```
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), for N > 1.
```
Given N, calculate F(N).

```
Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

```

```
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

```


```
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

```



### Code (python)

[Approach 1] (5%)

```python
class Solution:
    def fib(self, N: int) -> int:
        
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)
```

[Approach 2: Bottom-Up Approach using Memoization] (81%) (O(N))

```python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]
```

[Approach 3: Top-Down Approach using Memoization] (81%) (O(N))

```python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]
```
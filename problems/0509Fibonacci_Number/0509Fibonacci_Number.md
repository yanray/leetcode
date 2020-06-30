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

[Approach 3: Top-Down Approach using Memoization] (35%) (O(N))

```python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        self.cache = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
        return self.memoize(N)
```

[Approach 4: Iterative Top-Down Approach] (81%) (O(N))

```python
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N
        if (N == 2):
            return 1

        current = 0
        prev1 = 1
        prev2 = 1

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(3, N+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
```

https://leetcode.com/problems/fibonacci-number/solution/

[Approach 5: Matrix Exponentiation] (81%) (O(logN))

```python
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N-1)

        return A[0][0]

    def matrix_power(self, A: list, N: int):
        if (N <= 1):
            return A

        self.matrix_power(A, N//2)
        self.multiply(A, A)
        B = [[1, 1], [1, 0]]

        if (N%2 != 0):
            self.multiply(A, B)

    def multiply(self, A: list, B: list):
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w
```

[Approach 6: Math] (94%) (O(1))

```python
# Contributed by LeetCode user mereck.
class Solution:
  def fib(self, N):
  	golden_ratio = (1 + 5 ** 0.5) / 2
  	return int((golden_ratio ** N + 1) / 5 ** 0.5)
```
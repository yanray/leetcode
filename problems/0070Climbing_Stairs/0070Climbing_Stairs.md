## Climbing Stairs

### Problem Link
https://leetcode.com/problems/climbing-stairs/

### Problem Description 

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note:** Given n will be a positive integer.

```
Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

```
Example 2: 

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

### How to solve 

**Approach 1:** 

Dynamic Porgramming, dp[i] = dp[i - 1] + dp[i - 2], dp[1] = 1, dp[2] = 2

**Approach 2:** 

Fibonacci Number, Fibonacci Formula

```latex
\begin{equation}
    \sum_{\forall i}{x_i^{2}}
\end{equation}
```


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0070Climbing_Stairs/0070Climbing_Stairs1.py)

```python
ways = 0
first = 1
second = 2

if n == 1:
    return first
elif n == 2:
    return second
else:
    for i in range(2, n):
        ways = first + second
        first = second
        second = ways

return ways
```



## Single Number

### Problem Link
https://leetcode.com/problems/single-number/

### Problem Description 

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```
Example 1:

Input: [2,2,1]
Output: 1
```

```
Example 2: 

Input: [4,1,2,1,2]
Output: 4

```

### How to solve 

**Approach 1:** 

Dynamic Porgramming, dp[i] = dp[i - 1] + dp[i - 2], dp[1] = 1, dp[2] = 2

**Approach 2:** 

Fibonacci Number, Fibonacci Formula

![Fibonacci Formula](https://latex.codecogs.com/gif.latex?F_n%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt5%7D%5B%28%5Cfrac%7B1%20&plus;%20%5Csqrt5%7D%7B2%7D%29%5E2%20-%20%28%5Cfrac%7B1%20-%20%5Csqrt5%7D%7B2%7D%29%5E2%5D)

**Approach 3:** 

Use Binets Method to compute matrix multiplication to get the answer

**Approach 4:** 

Recursion with Memoization

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

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0070Climbing_Stairs/0070Climbing_Stairs2.py)

```python
def fib(n):
    sqrt5 = math.sqrt(5)
    Fn = (1 / sqrt5) * (((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n)

    return int(Fn)
return fib(n + 1)
```


[Approach 3]


[Approach 4](https://github.com/yanray/leetcode/blob/master/problems/0070Climbing_Stairs/0070Climbing_Stairs4.py)

```python
def helper(n: int) -> int:
    if n < 3:
        return n
    elif n not in memo:
        memo[n] = helper(n-1) + helper(n-2)
    return memo[n]

memo = {}
return helper(n)
```

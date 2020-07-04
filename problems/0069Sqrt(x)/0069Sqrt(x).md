## Sqrt(x)

### Problem Link

https://leetcode.com/problems/sqrtx/

### Problem Description 

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

```
Example 1:

Input: 4
Output: 2

```

```
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

```

### Code (python)

[Approach 1] (82%) (log(N))

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        elif x <= 3:
            return 1

        left, right = 2, x // 2        
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1
            else:
                return mid
        
        return right
```

[Approach 2: Math equation] (98%)

```python
from math import e, log
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = int(e**(0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right
```

https://leetcode.com/problems/sqrtx/discuss/559480/Python-implementation-of-the-algorithm-developed-for-EDSAC

https://leetcode.com/problems/sqrtx/discuss/427538/python3-One-Liner%3A-return-int(x-**-(12))

https://leetcode.com/problems/sqrtx/discuss/329955/Python-simple-differnt-solutions

[Approach 3: Newton method] (65%)

```python
class Solution:
    # Newton method
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:      
            r = (r*r+x)//(2*r)
             
        return r
```
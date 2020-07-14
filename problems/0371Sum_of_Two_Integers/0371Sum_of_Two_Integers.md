## Sum of Two Integers

### Problem Link

https://leetcode.com/problems/binary-tree-paths/

### Problem Description 

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

```
Example 1:

Input: a = 1, b = 2
Output: 3

```

```
Example 2:

Input: a = -2, b = 3
Output: 1

```

### Code (python)

[Approach 1] (51%) 

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry    
        else:
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow
            
        return x * sign
```

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)  
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign
```
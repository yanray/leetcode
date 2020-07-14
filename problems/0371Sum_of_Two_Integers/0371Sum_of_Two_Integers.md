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

[Approach 2] (76%)

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        def myadd(c, d):
            while d != 0:
                c, d = c^d, (c&d)<<1
            return c
        if a < 0 and myadd(~a, 1) <= b or b < 0 and myadd(~b, 1) <= a:
            return ~myadd(myadd(~a, ~b), 1)
        return myadd(a, b)
```

[Approach 3] (%)

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ## RC ##
        ## APPROACH : BITWISE OPERATIONS ##
        ## LOGIC ##
        #   1. For any two numbers, if their binary representations are completely opposite, then XOR operation will directly produce sum of numbers ( in this case carry is 0 )
        #   2. what if the numbers binary representation is not completely opposite, XOR will only have part of the sum and remaining will be carry, which can be produced by and operation followed by left shift operation.
        #   3. For Example 18, 13 => 10010, 01101 => XOR => 11101 => 31 (ans found), and operation => carry => 0
        #   4. For Example 7, 5
        #   1 1 1                   1 1 1
        #   1 0 1                   1 0 1
        #   -----                   -----
        #   0 1 0   => XOR => 2     1 0 1  => carry => after left shift => 1 0 1 0
        #   2                                                              10
        # now we have to find sum of 2, 10 i.e a is replace with XOR result and b is replaced wth carry result
        # similarly repeating this process till carry is 0
        #   steps will be 7|5 => 2|10 => 8|4  => 12|0
        
		## TIME COMPLEXITY : O(1) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a
```
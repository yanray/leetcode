## Reverse Integer

### Problem Link
https://leetcode.com/problems/reverse-integer/

**Extended Slices**

https://docs.python.org/2.3/whatsnew/section-slices.html

https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html

### Problem Description 

Given a 32-bit signed integer, reverse digits of an integer.

```
Example 1:

Input: 123
Output: 321

```

```
Example 2:

Input: -123
Output: -321

```


```
Example 3:

Input: 120
Output: 21

```


### How to solve 

**Approach 1**
判断正负, 求mod, 求商, 判断是否在范围内

**Approach 2**
转成string, 反转


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0007Reverse_Integer/0007Reverse_Integer1.py)

```python
lower_limit = -pow(2, 31)
upper_limit = pow(2, 31) - 1

rev_x = 0
if x < 0:
    sign = -1
    x = -x
else: 
    sign = 1

while x != 0:
    x, temp = divmod(x, 10)
    rev_x = rev_x * 10 + temp
rev_x = rev_x * sign
    
return rev_x if rev_x < upper_limit and rev_x > lower_limit else 0 
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0007Reverse_Integer/0007Reverse_Integer1.py)

```python
upper_limit = 2 ** 31 - 1
lower_limit = -2 ** 31

str_x = str(x)
if x >= 0:
    rev_x = int(str_x[::-1])
else:
    rev_x = int("-" + str_x[1:][::-1])
    
return rev_x if rev_x < upper_limit and rev_x > lower_limit else 0 
```
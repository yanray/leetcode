## Reverse Integer

### Problem Link
https://leetcode.com/problems/reverse-integer/

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

[My Submission](https://github.com/yanray/leetcode/blob/master/problems/0007Reverse_Integer/0007Reverse_Integer1.py)

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

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0001TwoSum/0001TwoSum2.py)

```python
h = {}
for i, num in enumerate(nums):
    n = target - num
    if n not in h:
        h[num] = i
    else:
        return [h[n], i]
```
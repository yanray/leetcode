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

[My Submission](https://github.com/yanray/leetcode/blob/master/problems/0001TwoSum/0001TwoSum1.py)

```python
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in nums:
        if i != nums.index(diff):
            return [i, nums.index(diff)]
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
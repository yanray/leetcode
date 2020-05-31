## Missing Number

### Problem Link

https://leetcode.com/problems/missing-number/

### Problem Description 

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

```
Example 1: 

Input: [3,0,1]
Output: 2

```

```
Example 2: 

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

```

### How to solve 

**Approach 1:** 

Use set(), then make difference to find the missing element

**Approach 2:** 

Sorting

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0268Missing_Number/0268Missing_Number1.py)

```python
whole_num_set = set(range(len(nums) + 1))
miss_num_set = set(nums)

return whole_num_set.difference(miss_num_set).pop()
```



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

**Approach 3:** 

Bit Manipulation

**Approach 3:** 

Gauss' Formula

![Gauss' Formula](https://latex.codecogs.com/gif.latex?%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%20i%20%3D%20%5Cfrac%7Bn%20%28n%20&plus;%201%29%7D%7B2%7D)

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0268Missing_Number/0268Missing_Number1.py)

```python
whole_num_set = set(range(len(nums) + 1))
miss_num_set = set(nums)

return whole_num_set.difference(miss_num_set).pop()
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0268Missing_Number/0268Missing_Number2.py)

```python
nums.sort()

for i in range(len(nums)):
    if i != nums[i]:
        return i

return len(nums)
```

[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0268Missing_Number/0268Missing_Number3.py)

```python
missing_num = len(nums)

for i, num in enumerate(nums):
    missing_num ^= i ^ num

return missing_num
```


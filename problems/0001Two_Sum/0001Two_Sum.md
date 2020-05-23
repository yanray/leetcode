## TwoSum

### Problem Link
https://leetcode.com/problems/two-sum/

### Problem Description 

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

```
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

```

### How to solve 
根据target的值求差，寻找差值是否在array里


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

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0001TwoSum/0001TwoSum3.py)

```python
hashtable = {}
for i in range(len(nums)):
    if nums[i] not in hashtable:
        hashtable[target-(nums[i])] = i
    else:
        return [hashtable[nums[i]], i]
```
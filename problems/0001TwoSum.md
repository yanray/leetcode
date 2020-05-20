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



### Code (python)

```diff
+ My Submission
```

```python
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in nums:
        if i != nums.index(diff):
            return [i, nums.index(diff)]
```

```diff
- Good Solution 1
```

```python
h = {}
for i, num in enumerate(nums):
    n = target - num
    if n not in h:
        h[num] = i
    else:
        return [h[n], i]
```

```diff
- Good Solution 2
```

```python
hashtable = {};
for i in range(len(nums)):
    if nums[i] not in hashtable:
        hashtable[target-(nums[i])] = i;
    else:
        return [hashtable[nums[i]], i];
```
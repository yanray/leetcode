## Two Sum II - Input array is sorted

### Problem Link

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

### Problem Description 

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

* Your returned answers (both index1 and index2) are not zero-based.
* You may assume that each input would have exactly one solution and you may not use the same element twice.

```
Example 1: 

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

```


### How to solve 

**Approach 1:** 

Use dictionary

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0015_3Sum/0015_3Sum.py)

```python
map_dict = {}
for i in range(len(numbers)):
    val = target - numbers[i]
    if val not in map_dict:
        map_dict[numbers[i]] = i
    else:
        return [map_dict[val] + 1, i + 1]
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0015_3Sum/0015_3Sum.py)

```python
map_dict = {}
for i in range(len(numbers)):
    val = target - numbers[i]
    if val not in map_dict:
        map_dict[numbers[i]] = i
    else:
        return [map_dict[val] + 1, i + 1]
```
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


**Approach 2:** 

Two pointers, one to low, the other to high


**Approach 3:** 

Binary Search

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0167Two_Sum_II/0167Two_Sum_II1.py)

```python
map_dict = {}
for i in range(len(numbers)):
    val = target - numbers[i]
    if val not in map_dict:
        map_dict[numbers[i]] = i
    else:
        return [map_dict[val] + 1, i + 1]
```


[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0167Two_Sum_II/0167Two_Sum_II2.py)

```python
low = 0
high = len(numbers) - 1

while low < high:
    sum = numbers[low] + numbers[high]
    if sum == target:
        return [low + 1, high + 1]
    if sum < target:
        low += 1
    else:
        high -= 1
        
return []
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/problems/0167Two_Sum_II/0167Two_Sum_II3.py)

```python
# binary search
for index, num in enumerate(numbers):
    new_target = target - num
    i, j = index + 1, len(numbers)-1
    # search the new value in numbers
    while i <= j:
        mid = (i + j)//2
        if numbers[mid] == new_target:
            return [index+1, mid+1]
        elif numbers[mid] > new_target:
            j = mid - 1
        else:
            i = mid + 1
```
## Find Pivot Index

### Problem Link

https://leetcode.com/problems/find-pivot-index/

### Problem Description 

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

```
Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

```

```
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

```


### Code (python)

[Approach 1] (77%) 

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        
        left_sum = 0
        index = 0
        while index < len(nums):
            total -= nums[index]
            
            if left_sum == total:
                return index
                
            left_sum += nums[index]
            index += 1
        
        return -1
```

[Approach 1] (99%) 

```python
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

```
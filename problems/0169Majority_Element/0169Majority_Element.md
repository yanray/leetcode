## Majority Element

### Problem Link

https://leetcode.com/problems/majority-element/

### Problem Description 


Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

```
Example 1:

Input: [3,2,3]
Output: 3

```

```
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

```

### How to solve 

**Approach 1:**


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0169Majority_Element/0169Majority_Element1.py)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash_dict = collections.Counter(nums)
        for k, v in hash_dict.items():
            if v >= len(nums) // 2 + 1:
                return k
```

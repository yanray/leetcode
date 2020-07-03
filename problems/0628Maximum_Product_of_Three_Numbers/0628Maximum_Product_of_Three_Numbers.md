## Maximum Product of Three Numbers

### Problem Link

https://leetcode.com/problems/maximum-product-of-three-numbers/

### Problem Description 

Given an integer array, find three numbers whose product is maximum and output the maximum product.

```
Example 1:

Input: [1,2,3]
Output: 6

```

```
Example 2:

Input: [1,2,3,4]
Output: 24

```

**Note:**

* The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
* Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

### Code (python)

[Approach 1] (95%)

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if nums[0] < 0 and nums[1] < 0:
            return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
        else:
            return nums[-3] * nums[-2] * nums[-1]
```
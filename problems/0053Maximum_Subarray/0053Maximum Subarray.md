## Maximum Subarray

### Problem Link
https://leetcode.com/problems/maximum-subarray/

### Problem Description 

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


```
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

```


### How to solve 

**Divide and Conquer:** https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/
把array细分，不短的求left sum, max cross sum, right sum, 最大值即所有可能性的最大值，max(left sum, cross sum, right sum). 


**Method 2:(Greedy)** 
array自左向右, 不断的找极大值, 并记录最大值, 最终返回最大值

**Method 3:**
array自左向右不, 断更新array的值, 如果nums[i - 1] >= 0, 表示前面的数组的sum值会使当前的nums[i]的值变大，则更新nums[i], 如果nums[i - 1] < 0, 反之。以此方法最终求得更新后的nums[i]的最大值, 也是最大的subarray.

​

### Code (python)

[Method 1]

```python

```

[Method 2]()

```python
max_sum = nums[0]
local_max_sum = nums[0]
for i in range(1, len(nums)):
    local_max_sum = max(nums[i], local_max_sum + nums[i])
    max_sum = max(max_sum, local_max_sum)
    
return max_sum
```

[Method 2]()

```python
max_sum = nums[0]
for i in range(1, len(nums)):
    if(nums[i - 1] >= 0):
        nums[i] += nums[i - 1]
    max_sum = max(nums[i], max_sum)
    
return max_sum
```

```python
for i in range(1, len(nums)):
    nums[i] = max(nums[i], nums[i-1]+nums[i])
    
return max(nums)
```
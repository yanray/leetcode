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

Divide and Conquer: https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/



​

### Code (python)

[Method 1](https://github.com/yanray/leetcode/blob/master/problems/0021Merge_Two_Sorted%20_Lists/0021Merge_Two_Sorted%20_Lists1.py)

```python
max_sum = nums[0]
local_max_sum = nums[0]
for i in range(1, len(nums)):
    local_max_sum = max(nums[i], local_max_sum + nums[i])
    max_sum = max(max_sum, local_max_sum)
    
return max_sum
```

[Dynamic Programing](https://github.com/yanray/leetcode/blob/master/problems/0021Merge_Two_Sorted%20_Lists/0021Merge_Two_Sorted%20_Lists2.py)

```python
if l1 is None:
    return l2
elif l2 is None:
    return l1
elif l1.val < l2.val:
    l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
else:
    l2.next = self.mergeTwoLists(l1, l2.next)
    return l2
```

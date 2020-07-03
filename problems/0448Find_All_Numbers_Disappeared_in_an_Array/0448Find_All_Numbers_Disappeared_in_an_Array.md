## Find All Numbers Disappeared in an Array

### Problem Link

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

### Problem Description 

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

```
Example 1:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

```

### Code (python)

[Approach 1] (65%)

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        result = []
        curr_val = 1
        for i in range(len(nums)):
            if curr_val == nums[i]:
                curr_val += 1
                continue
            elif curr_val < nums[i]:
                result.append(curr_val)
                curr_val += 1
                while curr_val < nums[i]:
                    result.append(curr_val)
                    curr_val += 1
                curr_val += 1
                
        while curr_val <= len(nums):
            result.append(curr_val)
            curr_val += 1
    
        return result
```




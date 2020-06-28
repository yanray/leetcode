## Search in Rotated Sorted Array II

### Problem Link

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

### Problem Description 

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

```
Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

```

```
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

```

**Follow up:**

* This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
* Would this affect the run-time complexity? How and why?

### Code (python)

[Approach 1] (95%)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            elif nums[left] == nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
```

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/386846/Two-Solutions-in-Python-3-(beats-~98)

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28303/Share-my-recursive-and-iterative-Python-solution-with-detailed-explanation-O(n)-worst-case

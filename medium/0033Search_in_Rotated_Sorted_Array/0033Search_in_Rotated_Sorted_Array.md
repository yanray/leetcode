## Search in Rotated Sorted Array

### Problem Link

https://leetcode.com/problems/search-in-rotated-sorted-array/

### Problem Description 

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

```
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

```

```
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

```

### Code (python)

[Approach 1] (72%)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] > nums[mid]:
                if nums[mid] > target:
                    left += 1
                    right = mid - 1
                else:
                    if nums[left] < target:
                        left += 1
                        right = mid - 1
                    else:
                        left = mid + 1
                        right -= 1
            else:
                if nums[left] > target:
                    left = mid + 1
                    right -= 1
                else:
                    if nums[mid] < target:
                        left = mid + 1
                        right -= 1
                    else:
                        left += 1
                        right = mid - 1
                    
        return -1
            
```

[Improved of apporach 1] (90%)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] > nums[mid]:
                if nums[mid] > target or nums[left] < target:
                    left += 1
                    right = mid - 1
                else:
                    left = mid + 1
                    right -= 1
            else:
                if nums[left] > target or nums[mid] < target:
                    left = mid + 1
                    right -= 1
                else:
                    left += 1
                    right = mid - 1
                    
        return -1
```


[Approach 2: One-pass Binary Search] (90%)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]: 
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
```

[Approach 3: Binary Search] (72%)

```python
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
                
        def search(left, right):
            """
            Binary search
            """
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
        
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1 
        
        rotate_index = find_rotate_index(0, n - 1)
        
        # if target is the smallest element
        if nums[rotate_index] == target:
            return rotate_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search(rotate_index, n - 1)
        # search on the left side
        return search(0, rotate_index)
```

https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/591611/Easy-Understand-or-Beat-90-or-SOLUTION-for-BOTH-33.-and-81.-or-BinarySearch-or-Time%3A-O(nlogn)



[Approach 4](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/525379/Very-Simple-and-Clever-Python-Solution-O(lg-N)-beating-88) (46%)

```python
class Solution:
    def __init__(self):
        self._lesser = None
        self._limit = None
    
    
    def _get_value(self, x):
        if self._lesser:
            return -math.inf if x >= self._limit else x
        else:
            return math.inf if x< self._limit else x
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
       
        self._limit = nums[0]  
        self._lesser = True if target < nums[0] else False
        
        lo = 0
        hi = n - 1
        
        while lo <= hi:
            
            mid = lo + (hi - lo) // 2
            
            if target > self._get_value(nums[mid]):
                lo = mid + 1
            elif target < self._get_value(nums[mid]):
                hi = mid - 1
            else:
                return mid
        return -1       
             
```
## Word Break

### Problem Link

https://leetcode.com/problems/word-break/

### Problem Description 

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

**Note:**

* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.

```
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

```

```
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

```

```
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

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

[Approach 4] (%)

```python

```
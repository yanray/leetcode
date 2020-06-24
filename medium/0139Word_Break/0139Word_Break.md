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
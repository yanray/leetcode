## Container With Most Water

### Problem Link

https://leetcode.com/problems/container-with-most-water/

### Problem Description 

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and n is at least 2.

```
Example 1:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

```

### Code (python)

[Approach 1] (%)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height) - 1
        
        curr_left = height[left]
        curr_right = height[right]
        max_area = (right - left) * min(curr_left, curr_right)
        
        while left < right:
            if curr_left < curr_right:
                left += 1
                while left < right and curr_left >= height[left]:
                    left += 1
                curr_left = height[left]
            else:
                right -= 1
                while left < right and curr_right >= height[right]:
                    right -= 1
                curr_right = height[right]
                
            max_area = max(max_area, (right - left) * min(curr_left, curr_right))

        return max_area
```
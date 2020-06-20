## Rectangle Overlap

### Problem Link

https://github.com/yanray/leetcode/blob/master/medium/1249Minimum_Remove_to_Make_Valid_Parentheses/1249Minimum_Remove_to_Make_Valid_Parentheses.md

### Problem Description 

A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

```
Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

```

```
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

```

**Notes:**

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.

### Code (python)

[Approach 1] (98%)

```python
        if rec2[0] >= rec1[2]:
            return False
        if rec2[1] >= rec1[3]:
            return False
        if rec2[2] <= rec1[0]:
            return False
        if rec2[3] <= rec1[1]:
            return False
        
        return True
```

```python
        if rec2[0] >= rec1[2] or rec2[1] >= rec1[3] or rec2[2] <= rec1[0] or rec2[3] <= rec1[1]:
            return False
        else:
            return True
```

[Approach 2] (99%)

```python
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0
```

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        width = min(rec1[2], rec2[2]) - max(rec1[0],
                                            rec2[0])  # min_right - max_left
        height = min(rec1[3], rec2[3]) - max(rec1[1],
                                             rec2[1])  # min_high - max_low
        return width > 0 and height > 0
```
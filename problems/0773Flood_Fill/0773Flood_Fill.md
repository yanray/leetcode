## Flood Fill

### Problem Link

https://leetcode.com/problems/flood-fill/

### Problem Description 

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

```
Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

```

**Note:**

* The length of image and image[0] will be in the range [1, 50].
* The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
* The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

### How to solve 

**Approach 1 - 2:**

DFS


### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0773Flood_Fill/0773Flood_Fill1.py)

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def helper(image, i, j, original_color, new_color):
            
            nr = len(image)
            nc = len(image[0])
            
            if i < 0 or i >= nr or j < 0 or j >= nc or image[i][j] != original_color:
                return 
            
            image[i][j] = new_color
            helper(image, i - 1, j, original_color, new_color)
            helper(image, i + 1, j, original_color, new_color)
            helper(image, i, j - 1, original_color, new_color)
            helper(image, i, j + 1, original_color, new_color)

        if image[sr][sc] == newColor:
            return image
    
        new_image = image.copy()
        # new_image = image
        helper(new_image, sr, sc, image[sr][sc], newColor)
        
        return new_image
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/problems/0773Flood_Fill/0773Flood_Fill2.py)

```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
```
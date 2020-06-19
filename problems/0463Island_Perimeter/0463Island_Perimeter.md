## Island Perimeter

### Problem Link

https://leetcode.com/problems/merge-intervals/

### Problem Description 

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


```
Example 1:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

```


### How to solve 

**Approach 1:**

**Approach 2:**

Simple Counting (数边)

**Approach 3:**

Better Counting (left and up)


### Code (python)

[Approach 1]

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
          
        nr = len(grid)
        nc = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    
        perimeter_count = copy.deepcopy(grid)
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    for d in directions:
                        r, c = i + d[0], j + d[1]
                        if r >= 0 and r < nr and c >= 0 and c < nc and grid[r][c] == 1:
                            perimeter_count[r][c] += 1
                            
        perimeter = 0              
        for i in range(nr):
            for j in range(nc):
                if perimeter_count[i][j] != 0:
                    perimeter += 5 - perimeter_count[i][j]
```

[Approach 2] (88.62%)

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0:
                        up = 0
                    else:
                        up = grid[r-1][c]
                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c-1]
                    if r == rows-1:
                        down = 0
                    else:
                        down = grid[r+1][c]
                    if c == cols-1:
                        right = 0
                    else:
                        right = grid[r][c+1]
                        
                    result += 4-(up+left+right+down)
                
        return result
```


[Approach 3] (95.62%)

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        result = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        
        return result
```

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                    if grid[row][column]:
                        res+=4
                        if row and grid[row-1][column]:
                            res-=2                        
                        if column and grid[row][column-1]:
                            res-=2
        return res
```
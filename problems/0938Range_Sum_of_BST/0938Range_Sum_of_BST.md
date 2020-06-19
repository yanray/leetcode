## Range Sum of BST

### Problem Link

https://leetcode.com/problems/range-sum-of-bst/

### Problem Description 

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.


```
Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

```

```
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

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
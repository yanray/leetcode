## Number of Islands

### Problem Link

https://leetcode.com/problems/number-of-islands/

### Problem Description 

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

```
Example 1: 

Input:
11110
11010
11000
00000

Output: 1

```

```
Example 2: 

Input:
11000
11000
00100
00011

Output: 3

```

### How to solve 

**Approach 1:** 




### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0200Number_of_Islands/0200Number_of_Islands1.py)

```python
if not grid:
    return 0

visited = grid.copy() # in case we do not want to modify our input
islands = 0
stack = [] # this will simulate the call stack 

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visited[i][j] != 'X' and grid[i][j] == '1':
            islands += 1
            stack.append((i, j))
            # perform dfs iteratively
            while stack:
                row, col = stack.pop()
                
                if grid[row][col] == '1' and visited[row][col] != 'X':
                    visited[row][col] = 'X'
                    
                if  row + 1 < len(grid) and grid[row + 1][col] == '1':
                    stack.append((row + 1, col))
                if  col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
                    stack.append((row, col + 1))
                if row - 1 >= 0 and grid[row - 1][col] == '1':
                    stack.append((row - 1, col))
                if col - 1 >= 0 and grid[row][col - 1] == '1':
                    stack.append((row, col - 1))
return islands
```


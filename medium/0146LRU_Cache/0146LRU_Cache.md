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

DFS: 访问过的Mark 为 "X", 每次访问到1即把周围的全Mark 为 "X"

**Approach 2:** 

DFS

**Approach 3:** 

BFS

**Approach 4:** 

Union Found



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


[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0200Number_of_Islands/0200Number_of_Islands2.py)

```python
#check if no input
numOfIslands = 0
if not grid or len(grid) == 0:
    return numOfIslands

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == '1':
            numOfIslands += 1 #found land. Increment the count by 1
            self.callDFS(grid, row, column) #call dfs to find the adjacent land. 
return numOfIslands

def callDFS(self, grid: List[List[str]], row, column):
nr = len(grid)
nc = len(grid[0])

# check for boundary conditions and the visited node.
if row < 0 or row >= nr or column < 0 or column >= nc or grid[row][column] == '0':
    return

grid[row][column] = '0' # mark the node as visited

# expand the search in adjacent directions.
self.callDFS(grid, row+1, column)
self.callDFS(grid, row-1, column)
self.callDFS(grid, row, column+1)
self.callDFS(grid, row, column-1)
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/medium/0200Number_of_Islands/0200Number_of_Islands3.py)

```python
count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "1":
            count += 1
            self.bfs(i, j, grid)

return count

def bfs(self, i: int, j: int, grid: List[List[str]]) -> None:
q = [(i, j)]

while q:
    i, j = q.pop(0)
    
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
        grid[i][j] = "0"
        q.append((i+1, j))
        q.append((i-1, j))
        q.append((i, j+1))
        q.append((i, j-1))
```


[Approach 4](https://github.com/yanray/leetcode/blob/master/medium/0200Number_of_Islands/0200Number_of_Islands4.py)

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0: return 0
        
        r, c = len(grid), len(grid[0])
        dsu = DSU(r * c)
        
        # union an island with its adjacent islands
        for i in range(r):
            for j in range(c):
                if int(grid[i][j]) == 1:
                    
                    # add this island first
                    dsu.numIsl += 1
                    
                    # union 4 adjacent islands if exist
                    if i - 1 >= 0 and int(grid[i - 1][j]) == 1:
                        dsu.union((i - 1) * c + j, i * c + j)
                    if i + 1 < r and int(grid[i + 1][j]) == 1:
                        dsu.union(i * c + j, (i + 1) * c + j)
                    if j - 1 >= 0 and int(grid[i][j - 1]) == 1:
                        dsu.union(i * c + (j - 1), i * c + j)
                    if j + 1 < c and int(grid[i][j + 1]) == 1:
                        dsu.union(i * c + j, i * c + (j + 1))
                            
        return dsu.numIsl
    
class DSU:
    def __init__(self, num):
        self.numIsl = 0
        self.par = list(range(num))
        self.rnk = [0] * num

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
			return
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.numIsl -= 1
```
## Rotting Oranges

### Problem Link

https://leetcode.com/problems/rotting-oranges/

### Problem Description 

In a given grid, each cell can have one of three values:

* the value 0 representing an empty cell;
* the value 1 representing a fresh orange;
* the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

```
Example 1: 

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

```

```
Example 2: 

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

```

```
Example 3: 

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

```

**Note:**
1. 1 <= grid.length <= 10
2. 1 <= grid[0].length <= 10
3. grid[i][j] is only 0, 1, or 2.

### How to solve 

**Approach 1:** 

Breadth-First Search (BFS)

**Approach 2:** 

In-place BFS https://en.wikipedia.org/wiki/In-place_algorithm

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/medium/0994Rotting_Oranges/0994Rotting_Oranges1.py)

```python
rotten_pos = []
num_fresh = 0
rotten_minutes = 0

num_r = len(grid)
num_c = len(grid[0])
for row in range(num_r):
    for col in range(num_c):
        if grid[row][col] == 2:
            rotten_pos.append((row, col))
        if grid[row][col] == 1:
            num_fresh += 1
if num_fresh == 0:
    return 0

while rotten_pos and num_fresh != 0:
    rotten_minutes += 1
    copy = rotten_pos
    rotten_pos = []
    for (i, j) in copy:
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            rotten_pos.append((i - 1, j))
            grid[i - 1][j] = 2
            num_fresh -= 1
        if i + 1 < num_r and grid[i + 1][j] == 1:
            rotten_pos.append((i + 1, j))
            grid[i + 1][j] = 2
            num_fresh -= 1
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            rotten_pos.append((i, j - 1))
            grid[i][j - 1] = 2
            num_fresh -= 1
        if j + 1 < num_c and grid[i][j + 1] == 1:
            rotten_pos.append((i, j + 1))
            grid[i][j + 1] = 2
            num_fresh -= 1
        
return rotten_minutes if num_fresh == 0 else -1
```

[Approach 2](https://github.com/yanray/leetcode/blob/master/medium/0994Rotting_Oranges/0994Rotting_Oranges2.py)

```python
ROWS, COLS = len(grid), len(grid[0])

# run the rotting process, by marking the rotten oranges with the timestamp
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def runRottingProcess(timestamp):
    # flag to indicate if the rotting process should be continued
    to_be_continued = False
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == timestamp:
                # current contaminated cell
                for d in directions:
                    n_row, n_col = row + d[0], col + d[1]
                    if ROWS > n_row >= 0 and COLS > n_col >= 0:
                        if grid[n_row][n_col] == 1:
                            # this fresh orange would be contaminated next
                            grid[n_row][n_col] = timestamp + 1
                            to_be_continued = True
    return to_be_continued

timestamp = 2
while runRottingProcess(timestamp):
    timestamp += 1
# end of process, to check if there are still fresh oranges left
for row in grid:
    for cell in row:
        if cell == 1:  # still got a fresh orange left
            return -1
# return elapsed minutes if no fresh orange left
return timestamp - 2
```


[Approach 3](https://github.com/yanray/leetcode/blob/master/medium/0994Rotting_Oranges/0994Rotting_Oranges3.py)

```python
# Constant for grid state
EMPTY = 0
FRESH = 1
ROTTEN = 2

# Get dimension of grid
h, w = len(grid), len(grid[0])

# record for fresh oranges
fresh_count = 0

# record for position of initial rotten oranges
rotten_grid = []        

for y in range(h):
    for x in range(w):
        
        if grid[y][x] == FRESH :
            fresh_count += 1
            
        elif grid[y][x] == ROTTEN:
            rotten_grid.append( (y, x, 0) )


if fresh_count == 0:
    # Quick response for no fresh organe
    return 0


traversal_queue = deque( rotten_grid )

# Launch BFS from rotten grid
while traversal_queue:
    
    cur_y, cur_x, time_stamp = traversal_queue.popleft()
    
    if 0 <= cur_y < h and 0 <= cur_x < w and grid[cur_y][cur_x] in (FRESH, ROTTEN):
        
        if grid[cur_y][cur_x] == FRESH:
            
            # This orange is rotten on current iteration
            # update fresh count
            fresh_count -= 1

            # Mark as visited with time stamp
            grid[cur_y][cur_x] = -time_stamp
            
            # update minute
            minute = time_stamp
    
        if ( grid[cur_y][cur_x] < 0 ) or ( time_stamp == 0 ):
            
            # BFS with new time stamp
            traversal_queue.append( (cur_y-1, cur_x, time_stamp+1) )
            traversal_queue.append( (cur_y+1, cur_x, time_stamp+1) )
            traversal_queue.append( (cur_y, cur_x-1, time_stamp+1) )
            traversal_queue.append( (cur_y, cur_x+1, time_stamp+1) )
        
# ----------------------------------------------------------------

if fresh_count == 0:
    # All orange is rotten finally
    return minute
else:
    # Some orange still keep fresh
    return -1
```
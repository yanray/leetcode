## Game of Life

### Problem Link

https://leetcode.com/problems/game-of-life/

### Problem Description 

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population..
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Given a non-empty string containing only digits, determine the total number of ways to decode it.

```
Example 1:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

```

**Follow up:**

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

### Code (python)

[Approach 1] (58%) 

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        nr = len(board)
        nc = len(board[0])
        
        check_matrix = []
        check_matrix.append([0 for i in range(nc + 2)])
        for i in range(nr):
            temp = [0]
            for j in range(nc):
                temp.append(board[i][j])
            temp += [0]
            check_matrix.append(temp)
        check_matrix.append([0 for i in range(nc + 2)])

        
        def update_cell(check_matrix, i, j):
            
            sum_val = 0
            direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for direct in direction:
                sum_val += check_matrix[i + direct[0]][j + direct[1]]
                
            if check_matrix[i][j] == 0:
                if sum_val == 3:
                    return 1
                else:
                    return 0
            else:
                if sum_val < 2 or sum_val > 3:
                    return 0
                else:
                    return 1
        
        for i in range(nr):
            for j in range(nc):
                board[i][j] = update_cell(check_matrix, i + 1, j + 1)
                
                
```


[Approach 2: O(mn) Space Solution] (80%) 

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
```

[Approach 3: O(1) Space Solution]

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Neighbors array to find 8 neighboring cells for a given cell
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    # row and column of the neighboring cell
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 signifies the cell is now dead but originally was live.
                    board[row][col] = -1
                # Rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # 2 signifies the cell is now live but was originally dead.
                    board[row][col] = 2

        # Get the final representation for the newly updated board.
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
```

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
                
        def liveNeighbors(i, j):
            nonlocal m, n
            return sum(board[x][y] & 1 for x in range(i-1, i+2) for y in range(j-1, j+2)
                       if not (x == i and y == j) and x >= 0 and y >= 0 and x < m and y < n)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = liveNeighbors(i, j)
				if board[i][j] & 1 == 1 and lives == 2 or lives == 3:
                    board[i][j] |= 2
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
```

```python
class Solution:
    def gameOfLife(self, m):
        mx,my=len(m),len(m[0])
        stat = [[0 for i in range(my)] for j in range(mx)]
        
        #count the cell amount
        for x in range(mx):
            for y in range(my):
                res = 0
                for i in (x-1,x,x+1):
                    for j in (y-1,y,y+1):
                        if (i==x and j==y) or not (0<=i<mx and 0<=j<my):
                            pass
                        else:
                            res += m[i][j]

                stat[x][y]=res
        
        #change
        for i in range(mx):
            for j in range(my):
                if m[i][j]:
                    if not 1<stat[i][j]<4:
                        m[i][j]=0
                else:
                    if stat[i][j]==3:
                        m[i][j]=1
```

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 0 -> 0 status = 0
        # 1 -> 1 status = 1
        # 1 -> 0 status = 2
        # 0 -> 1 status = 3
        m, n = len(board), len(board[0])
        directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        for x in range(m):
            for y in range(n):
                lives = 0
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<m and 0<=ny<n and (board[nx][ny] == 1 or board[nx][ny] == 2) :
                        lives+=1

                if board[x][y] == 0 and lives==3:
                    board[x][y] = 3
                elif board[x][y] == 1 and (lives<2 or lives>3):
                    board[x][y] = 2
        for x in range(m):
            for y in range(n):
                board[x][y] = board[x][y]%2
        return board
```

[Follow up 2 : Infinite Board]

```python
def gameOfLifeInfinite(self, live):
    ctr = collections.Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
    return {ij
            for ij in ctr
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

def gameOfLife(self, board):
    live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
    live = self.gameOfLifeInfinite(live)
    for i, row in enumerate(board):
        for j in range(len(row)):
            row[j] = int((i, j) in live)
```
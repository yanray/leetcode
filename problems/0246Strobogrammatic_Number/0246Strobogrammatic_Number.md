## Find Winner on a Tic Tac Toe Game

### Problem Link

https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

### Problem Description 

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

* Players take turns placing characters into empty squares (" ").
* The first player A always places "X" characters, while the second player B always places "O" characters.
* "X" and "O" characters are always placed into empty squares, never on filled ones.
* The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
* The game also ends if all squares are non-empty.
* No more moves can be played if the game is over.

Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

```
Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

```

```
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "

```

```
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

```

```
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "

```

**Constraints:**

* 1 <= moves.length <= 9
* moves[i].length == 2
* 0 <= moves[i][j] <= 2
* There are no repeated elements on moves.
* moves follow the rules of tic tac toe.


### Code (python)

[Approach 1] (58%) 

```python
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        def check(grid, ch, i, j):
            
            WIN = True
            
            for q in range(0, 3):
                if grid[i][q] != ch:
                    WIN = False
                    
            if WIN:
                return WIN
            
            WIN = True
            for q in range(0, 3):
                if grid[q][j] != ch:
                    print(grid[q][j])
                    WIN = False
                    
            return WIN
        
        
        if len(moves) <= 4:
            return "Pending"
        
        grid = [[0 for i in range(0, 3)] for i in range(0, 3)]
        
        TURN = True
        for move in moves:
            if TURN: # A turn
                grid[move[0]][move[1]] = "X"
                if check(grid, "X", move[0], move[1]):
                    return "A"
                
                TURN = False
                
            else: # B turn
                grid[move[0]][move[1]] = "O"
                if check(grid, "O", move[0], move[1]):
                    return "B"
                
                TURN = True
                
        print(grid)
                
        if (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]) or (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]):
            if grid[1][1] == "X":
                return "A"
            elif grid[1][1] == "O":
                return "B"
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
```

[Approach 2] (93%)

```python
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        for i in range(len(moves)):
            if i%2 == 0:
                player = 'A'
            else:
                player = 'B'
            board[moves[i][0]][moves[i][1]] = player
            transpose = [list(x) for x in zip(*board)]
            for num in range(3):
                if ''.join(board[num]) == player*3 \
                or ''.join(transpose[num]) == player*3 \
                or board[0][0]+board[1][1]+board[2][2] == player*3 \
                or board[0][2]+board[1][1]+board[2][0] == player*3:
                    return player
            if '-' not in board[0] and '-' not in board[1] and '-' not in board[2]:
                return 'Draw'
        return 'Pending'
```

[Approach 3] (93%)

```python
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        score = [[0]*8 for _ in range(2)]
        
        p = 0 #start with player A
        for i, j in moves:
            score[p][i] += 1
            score[p][3+j] += 1
            score[p][6] += (i == j)
            score[p][7] += (i+j == 2)
            if any(x == 3 for x in score[p]): return ["A", "B"][p]
            p ^= 1 #switch player
            
        return "Pending" if len(moves) < 9 else "Draw"
```

```
Explanation:
The key insight in my approach is based on the fact that you only need to check if the last player has won. To do this, find the location of the last move. We can call this location [x,y]. Based on the the total number of moves, one can deduce which player played last. The number of the player that played last is stored in P. We can also create a list which contains only Player A's moves and a list which contains only Player B's moves. These lists are stored in N. Next, we see if the row or column which contains the last move is full of the same symbol (X or Y). If it is, then the last player has won. If not, we check if either the main diagonal or the reverse diagonal is full of the same symbol (X or Y). If it is, then the last player has won. If the last move does not lead to a win (either in terms of row, column, or diagonal) then the result must be "Pending" or a "Draw". A draw will only happen if exactly 9 moves were made. Otherwise the result will be pending. It's important to note that it is always impossible for a player to win if they aren't the one making the last move. Only the player making the last move has the chance of winning. This fact simplifies things tremendously.
```

[Approach 4] (100%)

```python
class Solution:
    def tictactoe(self, M: List[List[int]]) -> str:
        L, P, [x,y], N = len(M), 1 - len(M) % 2, M[-1], [M[::2], M[1::2]]
        if all(p in N[P] for p in [[x,0],[x,1],[x,2]]) or all(p in N[P] for p in [[0,y],[1,y],[2,y]]): return ['A','B'][P]
        if all(p in N[P] for p in [[0,0],[1,1],[2,2]]) or all(p in N[P] for p in [[0,2],[1,1],[2,0]]): return ['A','B'][P]
        return ["Pending","Draw"][L == 9]
```


[Approach 5] (60%)

```python
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        class Score:
            def __init__(self):
                self.rows = [0 for i in range(3)]
                self.cols = [0 for i in range(3)]
                self.diag = 0
                self.adiag = 0
        A = Score()
        B = Score()
        for i, (x,y) in enumerate(moves):
            player = B if (i % 2) else A
            player.rows[x] += 1
            player.cols[y] += 1
            if (x == y):
                player.diag += 1
            if (x + y == 2):
                player.adiag += 1
                
            if 3 in A.rows or 3 in A.cols or A.diag == 3 or A.adiag == 3:
                return "A"
            if 3 in B.rows or 3 in B.cols or B.diag == 3 or B.adiag == 3:
                return "B"
            
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
```


[Approach 6] (93%)

```python
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        # List winner case
        win = [
            [(0,0),(0,1),(0,2)], [(0,0),(1,0),(2,0)],
            [(1,0),(1,1),(1,2)], [(0,1),(1,1),(2,1)],
            [(2,0),(2,1),(2,2)], [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
        ]
        
        # Distribute
        A = set(tuple(step) for step in moves[::2])
        B = set(tuple(step) for step in moves[1::2])
            
        # Check winner
        for win_case in win:
            if win_case[0] in A and win_case[1] in A and win_case[2] in A: return "A"
            if win_case[0] in B and win_case[1] in B and win_case[2] in B: return "B"
               
        # No winner
        if len(moves) == 9: return "Draw"
        else: return "Pending"
```
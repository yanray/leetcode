## Word Search

### Problem Link

https://leetcode.com/problems/word-search/

### Problem Description 

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

```
Example 1:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


```

**Constraints:**

* board and word consists only of lowercase and uppercase English letters.
* 1 <= board.length <= 200
* 1 <= board[i].length <= 200
* 1 <= word.length <= 10^3

### Code (python)

[Approach 1] (%) 

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(i,j,word,0,board):
                    return True
                
        return False
        
    def dfs(self,i , j, w,c,board):
        if c == len(w):
            return True
        
        if i < 0 or j >= len(board[0]) or i>= len(board) or j < 0 or board[i][j] != w[c]:
            return False
        
        temp = board[i][j]
        board[i][j] = ' '
        
        found = self.dfs(i+1,j,w,c+1,board) or self.dfs(i-1,j,w,c+1,board) or self.dfs(i,j+1,w,c+1,board) or self.dfs(i,j-1,w,c+1,board)
 
        board[i][j] = temp
    
        return found
```
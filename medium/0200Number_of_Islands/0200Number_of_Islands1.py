"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0;
        
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

if __name__ == '__main__':
 
    a = Solution()

    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print("Input: ")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = "")
        print()

    print("Output: ", a.numIslands(grid))



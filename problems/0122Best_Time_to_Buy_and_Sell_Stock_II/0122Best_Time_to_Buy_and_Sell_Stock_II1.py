"""

Version: 1.1 
Author:  Yanrui 
date:    06/10/2020
"""
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
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


if __name__ == '__main__':
    a = Solution()

    grid = [[2,1,1],[1,1,0],[0,1,1]]

    print("Input: ")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = "")
        print()

    print("Output: ", a.orangesRotting(grid))
    

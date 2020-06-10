"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
        
if __name__ == '__main__':
 
    a = Solution()

    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print("Input: ")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = "")
        print()

    print("Output: ", a.numIslands(grid))



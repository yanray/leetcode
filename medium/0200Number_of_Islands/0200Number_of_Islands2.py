"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
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
        
if __name__ == '__main__':
 
    a = Solution()

    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print("Input: ")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = "")
        print()

    print("Output: ", a.numIslands(grid))



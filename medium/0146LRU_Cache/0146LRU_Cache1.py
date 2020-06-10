"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/09/2020
"""

from typing import List

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
        
if __name__ == '__main__':
 
    a = Solution()

    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    print("Input: ")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = "")
        print()

    print("Output: ", a.numIslands(grid))



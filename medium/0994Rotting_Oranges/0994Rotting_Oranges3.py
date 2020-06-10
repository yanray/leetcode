"""

Version: 1.1 
Author:  Yanrui 
date:    06/10/2020
"""
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
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


if __name__ == '__main__':
    a = Solution()

    grid = [[2,1,1],[1,1,0],[0,1,1]]

    print("Input: ")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end = "")
        print()

    print("Output: ", a.orangesRotting(grid))
    

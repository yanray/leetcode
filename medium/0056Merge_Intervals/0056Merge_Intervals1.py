"""

Version: 1.1 
Author:  Yanrui 
date:    06/18/2020
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return intervals
        
        intervals = sorted(intervals, key = lambda x : x[0])
        output = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if right >= intervals[i][1]:
                continue
            if right >= intervals[i][0]:
                right = intervals[i][1]
            else:
                output.append([left, right])
                left, right = intervals[i][0], intervals[i][1]
        output.append([left, right])
            
        return output


if __name__ == '__main__':

    a = Solution()

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Input: ", intervals)
    print("Output: ", a.merge(intervals))



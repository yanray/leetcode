"""

Version: 1.1 
Author:  Yanrui 
date:    06/18/2020
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__ == '__main__':

    a = Solution()

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Input: ", intervals)
    print("Output: ", a.merge(intervals))



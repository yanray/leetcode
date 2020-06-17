"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 06/17/2020
"""

from typing import List

class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        def paint_cost(n, color):
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0: # Red
                total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
            elif color == 1: # Green
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
            else: # Blue
                total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
            return total_cost

        if costs == []:
            return 0
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))


if __name__ == '__main__':
    a = Solution()

    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print("input: ", costs)
    print("output: ", a.minCost(costs))





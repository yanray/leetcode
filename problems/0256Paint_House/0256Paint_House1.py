"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 06/17/2020
"""

from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        if not costs:
            return 0
        
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        
        return min(costs[-1])


if __name__ == '__main__':
    a = Solution()

    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print("input: ", costs)
    print("output: ", a.minCost(costs))





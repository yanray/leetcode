"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 06/17/2020
"""

from typing import List

class Solution:
    # O(1) space, shorter version, can be applied 
    # for more than 3 colors
    def minCost(self, costs):
        if not costs:
            return 0
        dp = costs[0]
        for i in range(1, len(costs)):
            pre = dp[:] # here should take care
            for j in range(len(costs[0])):
                dp[j] = costs[i][j] + min(pre[:j]+pre[j+1:])
        return min(dp)


if __name__ == '__main__':
    a = Solution()

    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print("input: ", costs)
    print("output: ", a.minCost(costs))





"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        # every loop, calculate the maximum cumulative amount of money until current house
        for i in nums:
            # as the loop begins，curr represents dp[k-1]，prev represents dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + i }
            prev, curr = curr, max(curr, prev + i)
            # as the loop ends，curr represents dp[k]，prev represents dp[k-1]

        return curr



if __name__ == '__main__':
    a = Solution()

    nums = [2,7,9,3,1]

    print(a.rob(nums))


    

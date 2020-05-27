"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import math

class Solution:
    def climbStairs(self, n: int) -> int:

        return int((1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n))

if __name__ == '__main__':
    a = Solution()

    n = 10
    print(a.climbStairs(n))


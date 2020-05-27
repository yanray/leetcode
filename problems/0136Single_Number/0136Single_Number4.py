"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import collections

class Solution:
    def singleNumber(self, nums) -> int:

        a = 0
        for n in nums:
            a ^= n
            
        return a

if __name__ == '__main__':
    a = Solution()

    nums = [4,1,2,1,2]
    print(a.singleNumber(nums))


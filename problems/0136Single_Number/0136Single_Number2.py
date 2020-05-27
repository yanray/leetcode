"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import collections

class Solution:
    def singleNumber(self, nums) -> int:

        hashmap = collections.Counter(nums)
        
        for n in nums:
            if hashmap[n] == 1:
                return n

if __name__ == '__main__':
    a = Solution()

    nums = [4,1,2,1,2]
    print(a.singleNumber(nums))


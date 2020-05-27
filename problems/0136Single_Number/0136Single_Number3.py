"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import collections

class Solution:
    def singleNumber(self, nums) -> int:

        hash_table = collections.defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i

if __name__ == '__main__':
    a = Solution()

    nums = [4,1,2,1,2]
    print(a.singleNumber(nums))


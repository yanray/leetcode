"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

import collections

class Solution:
    def singleNumber(self, nums) -> int:

        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

if __name__ == '__main__':
    a = Solution()

    nums = [4,1,2,1,2]
    print(a.singleNumber(nums))


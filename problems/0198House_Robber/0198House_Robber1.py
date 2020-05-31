"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        whole_num_set = set(range(len(nums) + 1))
        miss_num_set = set(nums)
        
        return whole_num_set.difference(miss_num_set).pop()


if __name__ == '__main__':
    a = Solution()

    nums = [9,6,4,2,3,5,7,0,1]

    print(nums)
    print(a.missingNumber(nums))


    

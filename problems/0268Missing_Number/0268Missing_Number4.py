"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == '__main__':
    a = Solution()

    nums = [9,6,4,2,3,5,7,0,1]

    print(nums)
    print(a.missingNumber(nums))


    

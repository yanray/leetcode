"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = len(nums)

        for i, num in enumerate(nums):
            missing_num ^= i ^ num

        return missing_num


if __name__ == '__main__':
    a = Solution()

    nums = [9,6,4,2,3,5,7,0,1]

    print(nums)
    print(a.missingNumber(nums))


    

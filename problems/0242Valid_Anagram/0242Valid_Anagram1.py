"""

Version: 1.1 
Author:  Yanrui 
date:    5/31/2020
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        nums = [0, 0, 0, 0] + nums
            
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])
            
        return max(nums)



if __name__ == '__main__':
    a = Solution()

    nums = [2,7,9,3,1]

    print(a.rob(nums))


    

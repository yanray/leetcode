"""

Version: 1.1 
Author:  Yanrui 
date:    5/27/2020
"""

class Solution:
    def singleNumber(self, nums) -> int:

        return sum(set(nums)) * 2 - sum(nums)

if __name__ == '__main__':
    a = Solution()

    nums = [4,1,2,1,2]
    print(a.singleNumber(nums))


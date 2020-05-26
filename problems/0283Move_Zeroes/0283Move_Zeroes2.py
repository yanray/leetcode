"""
if else 

Version: 1.1 
Author:  Yanrui 
date:      5/23/2020
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow, fast = 0, 0
        length = len(nums)
        for fast in range(length): 
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


if __name__ == '__main__':
    a = Solution()

    nums = [0,1,0,3,12] 

    print("Input: ", nums)

    a.moveZeroes(nums)
    print("Output: ", nums)

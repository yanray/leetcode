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
        
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                length -= 1
            else:
                i += 1


if __name__ == '__main__':
    a = Solution()

    nums = [0,1,0,3,12] 

    print("Input: ", nums)

    a.moveZeroes(nums)
    print("Output: ", nums)

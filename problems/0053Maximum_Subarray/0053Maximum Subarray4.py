"""
Merge Two Sorted Lists

Version: 1.1 
Author:  Yanrui 
date:    5/21/2020
"""

class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])
            
        return max(nums)




if __name__ == '__main__':
    a = Solution()

    ll = [-2,1,-3,4,-1,2,1,-5,4]

    print(a.maxSubArray(ll))



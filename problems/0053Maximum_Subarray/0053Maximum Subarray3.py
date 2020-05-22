"""
Merge Two Sorted Lists

Version: 1.1 
Author:  Yanrui 
date:    5/21/2020
"""

class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if(nums[i - 1] >= 0):
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
            
        return max_sum





if __name__ == '__main__':
    a = Solution()

    ll = [-2,1,-3,4,-1,2,1,-5,4]

    print(a.maxSubArray(ll))



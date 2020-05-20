"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                if i != nums.index(diff):
                    return [i, nums.index(diff)]


if __name__ == '__main__':
	s = Solution()
	nums = [2, 7, 11, 15]
	target = 9
	print(s.twoSum(nums, target))

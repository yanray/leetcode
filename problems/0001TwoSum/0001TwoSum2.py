"""
leetcode 0001 TwoSum
My submission

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def twoSum(self, nums, target):
        hashtable = {}
        for i, num in enumerate(nums):
            diff = target - num;
            if diff not in hashtable:
                hashtable[num] = i
            else
                return [hashtable[num], i]


if __name__ == '__main__':
	s = Solution()
	nums = [2, 7, 11, 15]
	target = 9
	print(s.twoSum(nums, target))

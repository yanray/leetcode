"""
leetcode 0002 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 5/20/2020
"""


class Solution:
    def twoSum(self, nums, target):
        hashtable = {}
        for i, num in enumerate(nums):
            # print('i', i)
            # print('num', num)
            diff = target - num;
            if diff not in hashtable:
                hashtable[num] = i          # save as dictionary
            else:
                # print('hashtable', hashtable)
                # print('diff', diff)
                # print('hashtable[diff]', hashtable[diff])
                return [hashtable[diff], i]


if __name__ == '__main__':
	s = Solution()
	nums = [2, 7, 11, 15]
	target = 9
	print(s.twoSum(nums, target))

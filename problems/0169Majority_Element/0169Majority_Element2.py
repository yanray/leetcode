"""
leetcode 0001 TwoSum

Version: 1.1 
Author:  Yanrui 
date: 	 06/17/2020
"""

from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] in hash_dict:
                hash_dict[nums[i]] += 1
            else:
                hash_dict[nums[i]] = 1
                
            if hash_dict[nums[i]] >= len(nums) // 2 + 1:
                return nums[i]


if __name__ == '__main__':
    a = Solution()

    nums = [3,2,3]
    print("input: ", nums)
    print("output: ", a.majorityElement(nums))





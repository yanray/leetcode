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
        
        hash_dict = collections.Counter(nums)
        for k, v in hash_dict.items():
            if v >= len(nums) // 2 + 1:
                return k


if __name__ == '__main__':
    a = Solution()

    nums = [3,2,3]
    print("input: ", nums)
    print("output: ", a.majorityElement(nums))





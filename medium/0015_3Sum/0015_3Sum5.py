"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i,v in enumerate(nums):
            self.twoSum(nums[i+1:],-v,ans)
        return ans
    
    def twoSum(self,nums,target,ans):
        d = {}
        for i,v in enumerate(nums):
            if target-v in d:
                ans.add((v,target-v,-target)) #3sum wants the numbers, while 2sum wanted the indices
            d[v] = i

if __name__ == '__main__':

	a = Solution()

	nums = [-1, 0, 1, 2, -1, -4]

	print("Input: ", nums)
	print("Output: ", a.threeSum(nums))



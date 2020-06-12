"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List
import bisect

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:

		nums.sort()
		i, s, n = 0, [], len(nums)
		while i < n-2 and nums[i] <= 0:
			l, r = i+1, n-1
			while l < r:
				m = nums[i]+nums[l]+nums[r]
				if m < 0: l += 1
				elif m > 0: r -= 1
				else:
					s.append([nums[i], nums[l], nums[r]])
					l = bisect.bisect_right(nums, nums[l], l, r)
					r = bisect.bisect_left(nums, nums[r], l, r)-1
			i = bisect.bisect_right(nums, nums[i], i)
		return s

if __name__ == '__main__':

	a = Solution()

	nums = [-1, 0, 1, 2, -1, -4]

	print("Input: ", nums)
	print("Output: ", a.threeSum(nums))



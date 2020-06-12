"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List
import bisect
import collections

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		cnt = collections.Counter(nums)
		s, n, key = [], len(cnt), sorted(cnt)
		for i, k in enumerate(key):
			if k < 0:
				q, r = divmod(-k, 2)                      # case a(-), c(+), c(+)
				if not r and cnt[q] > 1:
					s.append([k, q, q])
				l, r = i+1, n-1
				while l < r:                              # case a(-), b, c(+)
					m = key[i]+key[l]+key[r]
					if m < 0: l += 1
					elif m > 0: r -= 1
					else: 
						s.append([key[i], key[l], key[r]])
						l += 1
						r -= 1
			elif k > 0:                                   # case a(-), a(-), c(+)
				q, r = divmod(k, 2)
				if not r and cnt[-q] > 1:
					s.append([-q, -q, k])
			elif cnt[k] > 2: s.append([k, k, k])          # case k=0, i.e. b, b, b
		return s

if __name__ == '__main__':

	a = Solution()

	nums = [-1, 0, 1, 2, -1, -4]

	print("Input: ", nums)
	print("Output: ", a.threeSum(nums))



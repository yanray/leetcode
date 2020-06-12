"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        mapping = {}
        geq0 = set()
        leq0 = set()
        for i in nums:
            mapping[i] = 1 if i not in mapping.keys() else mapping[i] + 1
            if i >= 0:
                geq0.add(i)
            if i <= 0:
                leq0.add(i)
        
        for a in geq0:
            for b in leq0:
                c = - a - b
                potential = [a, b, c]
                if c in mapping.keys() and mapping[c] >= sum([x == c for x in potential]):
                    result.add(tuple(sorted(potential)))
        return result

if __name__ == '__main__':

	a = Solution()

	nums = [-1, 0, 1, 2, -1, -4]

	print("Input: ", nums)
	print("Output: ", a.threeSum(nums))



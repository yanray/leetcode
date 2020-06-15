"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/15/2020
"""

from typing import List

class Solution(object):
    def findPairs(self, nums, k):
        if k<0:
            return 0
        saw = set()
        diff = set()
        for i in nums:
            if i-k in saw:
                diff.add(i-k)
            if i+k in saw:
                diff.add(i)
            saw.add(i)
        return len(diff)

if __name__ == '__main__':

    a = Solution()
    nums = [3, 1, 4, 1, 5]
    k = 2

    print("Input: ", nums)
    print("k: ", k)
    print("Output: ", a.findPairs(nums, k))



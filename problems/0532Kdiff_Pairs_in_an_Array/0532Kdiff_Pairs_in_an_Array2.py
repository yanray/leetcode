"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/12/2020
"""

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int: 
        
        if not nums or k < 0:
            return 0
        
        nums.sort()

        N = len(nums)

        i = pairs = 0
        j = 1

        while j < N:
            if j < N - 1 and nums[j] == nums[j + 1]:
                j += 1

            elif nums[j] == nums[i] + k:
                pairs += 1
                i += 1
                j += 1

            elif nums[j] > nums[i] + k:
                i += 1

            elif nums[j] < nums[i] + k:
                j += 1

            j = max(j, i + 1)

        return pairs

if __name__ == '__main__':

    a = Solution()
    nums = [3, 1, 4, 1, 5]
    k = 2

    print("Input: ", nums)
    print("k: ", k)
    print("Output: ", a.findPairs(nums, k))



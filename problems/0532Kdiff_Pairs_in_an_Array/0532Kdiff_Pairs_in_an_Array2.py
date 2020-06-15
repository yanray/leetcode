"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/12/2020
"""

from typing import List
import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if not nums or k < 0:
            return 0
        
        output = 0
        if k == 0:
            for v in collections.Counter(nums).values():
                if v >= 2:
                    output += 1
            return output
        
        nums.sort()
        
        hash_dict = {}
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] in hash_dict:
                output += 1
            if nums[i] + k <= nums[-1]:
                hash_dict[nums[i] + k] = i
        if nums[-1] in hash_dict:
                output += 1
        
                
        # print(nums)
        # print(hash_dict)
        return output

if __name__ == '__main__':

    a = Solution()
    nums = [3, 1, 4, 1, 5]
    k = 2

    print("Input: ", nums)
    print("k: ", k)
    print("Output: ", a.findPairs(nums, k))



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
        ## RC ##
        ## LOGIC ##
        #   Boyer-Moore Voting Algorithm
        ## NOTE : WORKS ONLY IF ELEMENT OCCURENCE IS MORE THAN HALF OF ARRAY SIZE ##
        # Ex : [7, 7, 5, 7, 5, 1 , 5, 7 , 5, 5, 7, 7 , 7, 7, 7, 7]
        ## STACK TRACE ##
        ## count , candidate
        # 1 7
        # 2 7
        # 1 7
        # 2 7
        # 1 7
        # 0 7
        # 1 5
        # 0 5
        # 1 5
        # 2 5
        # 1 5
        # 0 5
        # 1 7
        # 2 7
        # 3 7
        # 4 7
        
        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(1) ##
        
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            #print(count, candidate)
        return candidate


if __name__ == '__main__':
    a = Solution()

    nums = [3,2,3]
    print("input: ", nums)
    print("output: ", a.majorityElement(nums))





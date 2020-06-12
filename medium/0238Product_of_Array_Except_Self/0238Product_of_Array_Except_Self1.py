"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/12/2020
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        nums_len = len(nums)
        from_left = [1]
        from_right = [1]
        product_nums = []
        
        for i in range(nums_len - 1):
            from_left.append(from_left[-1] * nums[i])
        
        for i in range(nums_len - 1, 0, -1):
            from_right.append(from_right[-1] * nums[i])
            
        for i in range(nums_len):
            product_nums.append(from_left[i] * from_right[nums_len - 1 - i])
            
        return product_nums
        
        from_left = [1]
        from_right = [1]
        product_nums = []
        
        for i in range(len(nums) - 1):
            from_left.append(from_left[-1] * nums[i])
        
        product_nums.append(from_left[-1])
        for i in range(len(nums) - 1, 0, -1):
            from_right.insert(0, from_right[0] * nums[i])
            product_nums.insert(0, from_right[0] * from_left[i - 1])
            
        return product_nums

if __name__ == '__main__':

	a = Solution()

	nums = [1,2,3,4]

	print("Input: ", nums)
	print("Output: ", a.productExceptSelf(nums))



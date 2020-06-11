"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # binary search
        for index, num in enumerate(numbers):
            new_target = target - num
            i, j = index + 1, len(numbers)-1
            # search the new value in numbers
            while i <= j:
                mid = (i + j)//2
                if numbers[mid] == new_target:
                    return [index+1, mid+1]
                elif numbers[mid] > new_target:
                    j = mid - 1
                else:
                    i = mid + 1


if __name__ == '__main__':

    a = Solution()

    numbers = [2,7,11,15]
    target = 9

    print("numbers: ", numbers)
    print("target: ", target)
    print("output: ", a.twoSum(numbers, target))



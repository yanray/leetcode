"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        low = 0
        high = len(numbers) - 1
        
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            if sum < target:
                low += 1
            else:
                high -= 1
                
        return []


if __name__ == '__main__':

    a = Solution()

    numbers = [2,7,11,15]
    target = 9

    print("numbers: ", numbers)
    print("target: ", target)
    print("output: ", a.twoSum(numbers, target))



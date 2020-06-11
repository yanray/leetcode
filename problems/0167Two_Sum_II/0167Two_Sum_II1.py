"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/11/2020
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        map_dict = {}
        for i in range(len(numbers)):
            val = target - numbers[i]
            if val not in map_dict:
                map_dict[numbers[i]] = i
            else:
                return [map_dict[val] + 1, i + 1]


if __name__ == '__main__':

    a = Solution()

    numbers = [2,7,11,15]
    target = 9

    print("numbers: ", numbers)
    print("target: ", target)
    print("output: ", a.twoSum(numbers, target))



"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/12/2020
"""

from typing import List
import numpy as np

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        s = []
        for i in range(len(items)):
            if i == 0 or items[i-1][0] != items[i][0]:                 
                s.append([items[i][0], sum(v for _, v in items[i:i+5])//5])
        return s

if __name__ == '__main__':

	a = Solution()

	nums = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

	print("Input: ", nums)
	print("Output: ", a.highFive(nums))



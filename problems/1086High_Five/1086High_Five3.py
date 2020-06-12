"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/12/2020
"""

from typing import List
import numpy as np

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        D = collections.defaultdict(list)
        for student, score in items:
            bisect.insort(D[student], score) # insert in a list in increasing order.
        return [[student, sum(D[student][-5:])//5] for student in D]

if __name__ == '__main__':

	a = Solution()

	nums = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

	print("Input: ", nums)
	print("Output: ", a.highFive(nums))



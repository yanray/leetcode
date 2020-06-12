"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/12/2020
"""

from typing import List
import numpy as np

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        high_five_dict = {}
        for i in range(len(items)):
            if items[i][0] in high_five_dict:
                if items[i][1] > high_five_dict[items[i][0]][0]:
                    high_five_dict[items[i][0]][0] = items[i][1]
                    high_five_dict[items[i][0]].sort()
            else:
                high_five_dict[items[i][0]] = [0, 0, 0, 0, items[i][1]]
            
        output = []
        for k, v in high_five_dict.items():
            output.append([k, int(np.mean(v))])
        
        return output

if __name__ == '__main__':

	a = Solution()

	nums = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

	print("Input: ", nums)
	print("Output: ", a.highFive(nums))



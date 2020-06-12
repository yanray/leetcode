"""

Version: 1.1 
Author:  Yanrui 
date: 	 06/12/2020
"""

from typing import List
import numpy as np

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # use collectioni for hashmap
        import collections
        # use heapq to get only top 5 values
        import heapq

        d = collections.defaultdict(list)
        # print(d)

        for idx, val in items:
            # adding values for each id in hashmap
            heapq.heappush(d[idx], val)
            # print(idx, val, d)

            if len(d[idx]) > 5:
                # print("if")
                # heappop pops the smallest value
                # so we alway has the length 5 for each id
                heapq.heappop(d[idx])
                # print(d)

        # print([[i, sum(d[i]) // 5] for i in sorted(d)])
        ans = [[i, sum(d[i]) // 5] for i in sorted(d)]
        return ans

if __name__ == '__main__':

	a = Solution()

	nums = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

	print("Input: ", nums)
	print("Output: ", a.highFive(nums))



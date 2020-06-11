"""

Version: 1.1 
Author:  Yanrui 
date:    06/10/2020
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))

if __name__ == '__main__':
    a = Solution()

    prices = [7,1,5,3,6,4]
    print("max profit: ", a.maxProfit(prices))
    

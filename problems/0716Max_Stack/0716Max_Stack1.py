"""

Version: 1.1 
Author:  Yanrui 
date:    06/10/2020
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if prices == sorted(prices, reverse = True):
        #     return 0
        
        valley = peak = 0
        len_price = len(prices)
        max_profit = 0
        i = 0
        while i < len_price - 1:
            while i < len_price - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            while i < len_price - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            max_profit += peak - valley
            
        return max_profit


if __name__ == '__main__':
    a = Solution()

    prices = [7,1,5,3,6,4]
    print("max profit: ", a.maxProfit(prices))
    

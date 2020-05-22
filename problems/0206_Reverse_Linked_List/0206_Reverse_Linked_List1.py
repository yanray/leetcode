"""

Version: 1.1 
Author:  Yanrui 
date: 	 5/22/2020
"""


class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        if len(prices) > 1:
            min_price = prices[0]

            for i in range(1, len(prices)):
                if prices[i] < min_price:
                    min_price = prices[i]
                max_profit = max(max_profit, prices[i] - min_price)

        return max_profit

if __name__ == '__main__':
    a = Solution()

    prices = [7,1,5,3,6,4]
    print(a.maxProfit(prices))



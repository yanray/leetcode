## Best Time to Buy and Sell Stock

### Problem Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Problem Description 

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.


```
Example1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

```

```
Example2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

```


### How to solve 

**Method:** 
Dynamic Programming: 

最大收益 = max(前i - 1天的最大收益, 第i天的股票价格 - 前i - 1天的最小股票价格)



### Code (python)

[Method](https://github.com/yanray/leetcode/blob/master/problems/0121Best_Time_to_Buy_and_Sell_Stock/0121Best_Time_to_Buy_and_Sell_Stock.py)

```python
max_profit = 0
if len(prices) > 1:
    min_price = prices[0]

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_profit = max(max_profit, prices[i] - min_price)

return max_profit
```

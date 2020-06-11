## Best Time to Buy and Sell Stock II

### Problem Link

https://leetcode.com/problems/rotting-oranges/

### Problem Description 

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

```
Example 1: 

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

```

```
Example 2: 

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

```

```
Example 3: 

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

```

Constraints:

* 1 <= prices.length <= 3 * 10 ^ 4
* 0 <= prices[i] <= 10 ^ 4

### How to solve 

**Approach 1:** 

Peal Vally Approach: 
![Peal Vally Approach](https://latex.codecogs.com/gif.latex?TotalProfit%20%3D%20%5Csum_i%28height%28peak_i%29%20-%20height%28valley_i%29%29)

### Code (python)

[Approach 1](https://github.com/yanray/leetcode/blob/master/problems/0122Best_Time_to_Buy_and_Sell_Stock_II/0122Best_Time_to_Buy_and_Sell_Stock_II1.py)

```python
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
```

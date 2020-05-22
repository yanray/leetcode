## Reverse Linked List

### Problem Link
https://leetcode.com/problems/reverse-linked-list/

### Problem Description 

Reverse a singly linked list.

```
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
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
